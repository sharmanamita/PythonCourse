class person:
    fname = "namita";lname="sharma"
    job = "developer"

    def printFullName(self): #self is compulsary
        print(self.fname, self.lname)

    def showJobProfile(this, message): #you use any keyword for self
        print(this.fname, "works as a", this.job, message.upper())

    @staticmethod
    def add(a, b):
        print("sum is ", a+b)

obj = person()
print(obj)
print(obj.fname, obj.lname, obj.job)
obj.fname = "Anita"

obj.printFullName()
obj.showJobProfile('How are you?')

person.add(1,2) #you call function directly using class name
person