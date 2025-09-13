from DBConnect.crud import getConnection, update, read, mydb, mycommit, myrollback, setcommit
import mysql.connector

def createAccountTable():
    cursor = getConnection()
    query = "CREATE TABLE account(account_no INT NOT NULL AUTO_INCREMENT,  name VARCHAR(255), balance VARCHAR(255), PRIMARY KEY(account_no))"
    cursor.execute(query)

def showRecords():
    cursor = getConnection()
    results = read('account')
    print(results)

def updateAccount(type, amount, accNo):
    cursor = getConnection()
    updateQuery = ""
    if type == 'withdraw':
        updateQuery = f"UPDATE account SET balance=balance-{amount} WHERE account_no={accNo}"
    else:
        updateQuery = f"UPDATE account SET balance=balance+{amount} WHERE account_no={accNo}"

    cursor.execute(updateQuery)

# createAccountTable()
try:
    setcommit(True)
    showRecords()
    updateAccount('withdraw', 500, 1)
    updateAccount('deposit', 100, 2)
    mycommit()
    showRecords()
except (mysql.connector.Error) as error:
    print(error)
    myrollback()
    showRecords()
