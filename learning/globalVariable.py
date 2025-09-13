alpha = 45
x =20


def getX():
    #x=40 #local var
    global x #use global var
    x=40

getX()
print(x)

y=35
if x>20: #global local concept is only applicable for functions / not for lines outside the functions
    y=100
    if x<=40:
        y +=1
        print(y)
    print(y)

print(y)