import random
from datetime import date

from DBConnect.crud import insertIntoUser, update, delete, read, myrollback, mycommit

# query = "CREATE TABLE product(id SMALLINT,  pname VARCHAR(255), pdesc VARCHAR(255), unitCost int, expiryDate DATE)"

while True:
    print('Menu',
          "1. Insert",
          "2. Read",
          "3. Update",
          "4. Delete",
          "5. Quit", sep="\n")

    choice = int(input("Please select:"))

    if choice == 1:
        id = random.randint(0,10)
        pname = input("Please enter product name:")
        pdesc = input("Please enter product description:")
        unitcost = int(input("Please enter product unit cost:"))
        d = input("Please enter product expirydate (dd/mm/yyyy):")
        dates = list(map(lambda x: int(x), d.split("/")))
        expirydate = date(day=dates[0], month=int(dates[1]), year=int(dates[2]))

        values = (id, pname, pdesc, unitcost, expirydate)
        insertIntoUser('product', values)
    elif choice == 2:
        read('product')
    elif choice == 3:
        id = int(input("Enter user Id:"))
        value = int(input("Enter value for unit cost:"))
        update(id, value, 'product')
    elif choice == 4:
        id = int(input("Enter user Id:"))
        delete(id, 'product')
    elif choice == 5:
        break