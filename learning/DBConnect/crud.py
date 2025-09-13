from datetime import date

import mysql.connector

mydb = None
def getConnection():
    global mydb
    if mydb is None:
        print("In mydb if")
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql',
            database='pythondb'
        )

    # mydb.autocommit = True
    return mydb.cursor()

def setcommit(flag):
    getConnection()

    global  mydb
    mydb.autocommit = flag

def mycommit():
    global mydb
    mydb.commit()

def myrollback():
    global mydb
    if mydb is not None:
        mydb.rollback()

def insertIntoUser(tableName, values):
    cursor = getConnection()

    insertQuery = f"INSERT INTO {tableName} (id,pname,pdesc,unitcost,expirydate) values (%s, %s ,%s ,%s ,%s)"
    print(values)

    cursor.execute(insertQuery, values)

def insertPerson(values):
    cursor = getConnection()
    insertQuery = f"INSERT INTO person (fname, lname, dob, city) values (%s ,%s ,%s ,%s)"
    cursor.execute(insertQuery, values)
    return cursor.lastrowid
	
def insert(tablename, columns, values):
    cursor = getConnection()
    insertQuery = f"INSERT INTO {tablename} (fname,lname,username,password) values (%s ,%s ,%s ,%s)"
    print(insertQuery)
    cursor.execute(insertQuery, values)
    return cursor.lastrowid

def read(tableName):
    cursor = getConnection()
    cursor.execute(f"SELECT * FROM {tableName}")
    records = cursor.fetchall()
    for row in records:
        print(row)
    return records

def update(id, value, tableName):
    cursor = getConnection()
    setcommit(False)
    updateQuery = f"UPDATE {tableName} SET unitcost=%s WHERE id=%s"
    cursor.execute(updateQuery, (value, id))

def delete(id, tableName):
    cursor = getConnection()
    updateQuery = f"DELETE FROM {tableName} WHERE id={id}"
    cursor.execute(updateQuery)

def getDataById(id, tableName):
    cursor = getConnection()
    cursor.execute(f"SELECT * FROM {tableName} WHERE id={id}")
    data = cursor.fetchone()
    # cursor.close()
    return data
	
def getLoginByUnameAndPwd(uname, pwd):
    cursor = getConnection()
    cursor.execute("SELECT * FROM login where username=%s and password=%s", (uname, pwd))
    data = cursor.fetchone()
    return data


# print(getLoginByUnameAndPwd('namishar', 'Namu@1234'))
	
