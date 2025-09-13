userLoginDict = {}

details = input("Please enter name & password to signup:")
unamepwd = details.split(",")

uname = unamepwd[0]
pwd = unamepwd[1]

userLoginDict[uname] = ~int(pwd)

while True:
    print("Menu",
          "1.Login - uname ,password",
          "2. change password",
          "3. show all uname and passwords",
          "4. Quit", sep='\n')
    menu = input("Please enter your choice:")

    if menu == "1":
        credentails = input("Please enter your credentails:")
        uname = credentails.split(",")[0]
        pwd = credentails.split(",")[1]

        if uname in userLoginDict:
            if int(pwd) == ~userLoginDict[uname]:
                print("Logged in Successfully")
            else:
                print("Login Failed")

    if menu == "2":
        username = input("Please enter your username:")
        originalpwd = input("Please enter your original password:")

        if username in userLoginDict:
            if int(originalpwd) == ~userLoginDict[username]:
                newpwd = input("Please enter your new password:")
                userLoginDict[username] = ~int(newpwd)
                print("Password changed Successfully")
            else:
                print("User not found")

    if menu == "3":
        print(userLoginDict)

    if menu == "4":
        break



