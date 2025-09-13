def f1(c1=1, c2=1):
    print('c1: ', c1, "c2:", c2)
    print('hello')

f1(10)
f1(c2=30)

def f2(*num): #this creates tuple
    sum=0
    print(num)
    #num[0]=25 #cannot modify as it is tuple
    for i in num:
        sum = sum + i
    print(sum)
f2(1,2,3,4,5,6,7,89,85)

# keyword-only arguments
def f3(**info):#this creates dictionary
    print(info)

f3(name= 'namita', age= 25)

def mix(x, y,*num):
    print(num, x, y)

mix(10,20,30,40,50)

def mix2(*num, **data):
    print(num, data)

mix2(10,20,30,name='nmaita', age=25)

def printlist(list):
    print(list)

printlist({'abc', 'xyz', 10, 20, 30})

def returnList(list):
    return list[0],list[2]

x = returnList([54,55,66])
print(x)