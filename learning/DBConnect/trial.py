import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql',
    database='pythondb'
)

# mydb.autocommit = True
updateQuery = "UPDATE account SET balance=balance-500 WHERE account_no=2"
mydb.cursor().execute(updateQuery)
# mydb.commit()