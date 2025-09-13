from Employee import Employee
from ExceptionEx.AgeException import AgeException

while True:
    print("Menu",
          "1. Create Employee",
          "2. Change age ",
          "3. Show details of all employees",
          "4. Quit", sep="\n")
    choice = int(input("Please select:"))

    if choice == 1:
        try:
            name = input("Please enter name:")
            age = input("Please enter age:")
            employee = Employee(name, int(age))
        except (AgeException) as e:
            print("Cannot add employee", e)
        except (ValueError) as error:
            print(error)
            continue
        except (Exception) as e1:
            print(e1)
    elif choice == 2:
        try:
            employee.changeAge()
        except (AgeException) as e:
            print("Cannot change age", e)
        except (Exception) as e1:
            print(e1)
    elif choice == 3:
        employee.show()
    elif choice == 4:
        break

