import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="pythondb"
)

cursor = mydb.cursor()
# cursor.execute("CREATE TABLE user(name VARCHAR(255), address VARCHAR(255))")
# query1 = "INSERT INTO user(name,address) values(%s, %s)"
#
# name = input("Enter your name:")
# address = input("Enter your address:")
# values = (name, address)
#
# cursor.execute(query1, values)
# mydb.commit()

# query2 = "UPDATE user SET name=:name where address=:address"
# cursor.execute(query2, {'name': 'Namita', 'address': 'Kothrud'})
# mydb.commit()

query3 = "SELECT * FROM user"
cursor.execute(query3)

results = cursor.fetchall()
for row in results:
    print(row[0])

print(cursor.rowcount)



