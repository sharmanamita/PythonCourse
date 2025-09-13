import mysql.connector

mydb = None
def getDbConnection():
    global mydb
    mydb = mysql.connector.connect(
        host= "localhost",
        user= "root",
        password="mysql",
        database="pythondb"
    )

    return mydb.cursor()    
    
def validateUserCredentials(uname, pwd):
    cursor = getDbConnection()
    cursor.execute("SELECT * FROM login where username=%s and password=%s", (uname, pwd))
    data = cursor.fetchone()
    return data 

def getNextQuestion(id):
    cursor = getDbConnection()
    cursor.execute(f"SELECT * FROM questionbank WHERE qid={id}")
    row = cursor.fetchone()

    columns = [description[0] for description in cursor.description]
    data = dict(zip(columns, row))

    # startLimit = (limit - 10) + 1
    # endLimit = limit
    # cursor.execute(f"SELECT * FROM questionbank WHERE qid BETWEEN {startLimit} AND {endLimit}")
    
    # columns = [description[0] for description in cursor.description]
    # data = [dict(zip(columns, row)) for row in rows]
    # print({'data': data, 'lastrowid': cursor.rowcount})
    # return {'data': data, 'lastrowid': cursor.rowcount}

    print(data)
    return data


def createResponse(status, message, results=None, token=None):
    response = {
        "status": status,
        "message": message,
    }

    if results is not None and token is not None:
        response['data'] = results
        response['token'] = token

    return response
