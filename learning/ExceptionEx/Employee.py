from ExceptionEx.AgeException import AgeException

class Employee:
    employeeList = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.validateAge(name, age, 'new')

    def show(self):
        print("Empoyee List as below:", self.employeeList)

    def changeAge(self):
        uname = input("Please enter employee name:")
        newage = int(input("Please enter age:"))
        return self.validateAge(uname, newage, 'update')

    def validateAge(self,uname, age, flag):
        if(age > 18 and age < 80):
            if flag == 'new':
                self.employeeList.append({uname: age})
            elif flag == 'update':
                self.employeeList[uname] = age
        else:
            raise AgeException("Age is not valid!")



