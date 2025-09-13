import json
import sys
sys.path.append("../")
from flask import Flask, request
from DBConnect.crud import setcommit, mycommit, getLoginByUnameAndPwd, insert

arr = [{'id': 1, 'uname': 'namita', 'password': 'namu123'}, { 'id': 2, 'uname': 'suman', 'password': 'suman123'}]
app = Flask(__name__)

@app.post('/api/login')
def getlogin():
    jsondata = request.get_json()
    uname = jsondata['uname']
    pwd = jsondata['password']
    print(uname, pwd)
    data = getLoginByUnameAndPwd(uname=uname, pwd=pwd)
    print(json.dumps(data))
    return json.dumps(data)


@app.post('/api/add')
def addUser():
    jsondata = request.get_json()
    setcommit(True)
    values = (jsondata['fname'], jsondata['lname'], jsondata['uname'], jsondata['password'])
    columns = ('fname', 'lname', 'username', 'password')
    print(columns, values)
    id = insert('login', columns=columns, values=values)
    mycommit()
    return json.dumps(id)
    

@app.post('/addmany')
def addmany():
    users = request.get_json()
    print(users)
    for user in users:
        print(user['uname'])
    return 'done'

@app.get('/getuser')
def getData():
    id = request.args.get('id')
    details = None
    for user in arr:
        if user['id'] == int(id):
           details = json.dumps(user)

    return details


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run()