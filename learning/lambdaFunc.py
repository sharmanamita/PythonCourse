def welcome(name):
    print("Welcome " + name)


def activity(f):
    f('suman')

activity(welcome)

func1 = lambda name: print(name.upper())
activity(func1)

#here x is function and can be called it out
x = lambda a,b: True if a > b else False

if x(10,20):
    print("a is greater than b")
else:
    print("a is not greater than b")

y = (lambda color: "small string" if len(color) <= 3 else "big string")("Red")
print(y)