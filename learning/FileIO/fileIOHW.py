# appendfile = open("./credentials.txt", 'r+')
# readfile = open("./credentials.txt", 'r')

class UserLogin:
    def __init__(self):
        self.credentailsDict = {}

    def createLogin(self):
        while True:
            uname = input("Please enter your user name:")

            if uname != '-1':
                pwd = input("Please enter your new password:")
                appendfile = open("./credentials.txt", 'r+')
                appendfile.write(uname + ":" + pwd + "\n")
                appendfile.close()
            else:
                # appendfile.close()
                break


    def populateDict(self):
        user = "start"
        readfile = open("./credentials.txt", 'a')
        while user != '':
            try:
                user = readfile.readline()
                cred = user.split(":")
                if len(cred) == 2:
                    if '\n' in cred[1]:
                        self.credentailsDict.update({cred[0]: cred[1][0: len(cred[1]) - 1]})
                    else:
                        self.credentailsDict.update({cred[0]: cred[1]})
            except (ValueError, UnboundLocalError) as e:
                readfile = open("./credentials.txt", 'a')

        readfile.close()
        print(self.credentailsDict)

    def login(self):
        uname = input("User Name:")
        pwd = input("Password:")
        if uname in self.credentailsDict:
            if self.credentailsDict[uname] == pwd:
                print("loggedIn Sucessfully!")
            else:
                print("Incorrect password!")
        else:
            print("User not Found!")

    def changepwd(self):
        uname = input("User Name:")
        oldpwd = input("Old Password:")
        newpwd = input("New Password:")
        appendfile = open("./credentials.txt", 'r+')
        readfile = open("./credentials.txt", 'r+')

        if uname in self.credentailsDict:
            if self.credentailsDict[uname] == oldpwd:
                self.credentailsDict[uname] = newpwd

                line = "start"
                content = ""
                while line != "":
                    print(line)
                    x = readfile.tell()
                    line = readfile.readline()
                    if uname in line:
                        print("here")
                        content = line.replace(oldpwd, newpwd)
                        appendfile.seek(x)
                        appendfile.write(content)
                        print("Password changed sucessfully!")
            else:
                print("Incorrect password!")
        else:
            print("User not Found!")
        appendfile.close()
        readfile.close()

while True:
    print("Menu", "1.Sigup", "2.Login", "3.Change password", "4.Quit", sep="\n")
    choice = int(input("Select above:"))
    user = UserLogin()
    user.populateDict()

    if choice == 1:
        user.createLogin()
        user.populateDict()
    elif choice == 2:
        user.login()
    elif choice == 3:
        user.changepwd()
        user.populateDict()
    elif choice == 4:
        break




