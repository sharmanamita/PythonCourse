
def greeting():
    print("Welcome", "Namita")

def decorator1(func):
    print("***************")
    return func

def decorator2(func):
    print(">>>>>>>>>>>>>>>")
    return func

# decoratorFunc = decorator2(decorator1(greeting))()

@decorator2
@decorator1
def mygreeting(name):
    print("Welcome ", name)

mygreeting("Priya")
