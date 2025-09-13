from datetime import datetime, date

from flask import Flask, request
from library1 import calcFactoral, calcSum, getMinorsAndAdults
from DBConnect.crud import getConnection, setcommit, mycommit, read, getDataById, myrollback, delete, insertPerson
import mysql.connector
app = Flask(__name__)

@app.route('/')
def f1():
    return f"Hello World!!"

@app.route('/factorial')
def f2():
    num = int(request.args.get('num'))
    return f"Factorial of {num} is {calcFactoral(num)}"

@app.route('/sum/<num1>/<num2>/<num3>/<num4>')
def f3(num1, num2, num3, num4):
    return f"Sum of {num1} + {num2} + {num3} + {num4} = {calcSum(num1, num2, num3, num4)}"


@app.get('/get')
def getData():
    details = None
    id = int(request.args.get('id'))
    try:
        setcommit(True)
        # results = read('person')
        # details = list(filter(lambda x:x[0] == id, results))
        # details = details[0]
        # print("details:", details[1])

        details = getDataById(id, 'person')
    except (mysql.connector.Error) as error:
        print(error)

    # return 'details'
    return f"id = {details[0]}, \n Name = {details[1]} {details[2]}, \n dob = {details[3].strftime('%d/%m/%Y')}, \n city = {details[4]}"

@app.delete('/delete/<id>')
def deletePerson(id):
    setcommit(True)
    delete(id, 'person')
    mycommit()
    return read('person')

@app.get('/getage')
def getAge():
    id = int(request.args.get('id'))
    records = read('person')
    details = list(filter(lambda x:x[0] == id, records))
    details = details[0]
    now = date.today()
    return f"Name: {details[1]} {details[2]}, Age: {now.year - details[3].year} years"

@app.put('/changecity/<id>/<newcityname>')
def changeCity(id, newcityname):
    cursor = getConnection()
    setcommit(True)
    updateQuery = f"UPDATE person SET city=%s WHERE id=%s"
    cursor.execute(updateQuery, (newcityname, id))
    mycommit()
    return read('person')

@app.get('/api/minors')
def getMinors():
    results = read('person')
    return getMinorsAndAdults(results, 'minors')

@app.get('/adults')
def getAdults():
    results = read('person')
    return getMinorsAndAdults(results, 'adults')

@app.post('/add/<fname>/<lname>/<dob>/<city>')
def insert(fname, lname, dob, city):
    d = dob.split('-')
    setcommit(True)
    newid = insertPerson((fname, lname, date(day=int(d[0]), month=int(d[1]), year=int(d[2]) ), city))
    mycommit()
    return f"Here is your id {newid}"

############################ End of basic get mapping

@app.get('/example')
def getEx():
    print("InGET::")
    return "GET"

@app.post('/example')
def postEx():
    print("InPOST::")
    return "POST"

@app.put('/example')
def putEx():
    print("InPUT::")
    return "PUT"

@app.delete('/example')
def deleteEx():
    print("InDelete::")
    return "InDelete"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run()