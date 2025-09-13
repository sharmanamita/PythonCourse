
def printName1(*names):
    print("Printing names one below another:", *names, sep="\n")

def printName2(*names):
    print("Printing names with coma separated:", *names, sep=",")

def printName3(*names):
    print("Printing names with indexes:")
    for name in range(0, len(names)):
        print(name+1, '.', names[name])


def formatName(*names, formatfunc):
    formatfunc(*names)

formatName("namita", "priya", "suman", "anita", formatfunc=printName1)
formatName("namita", "priya", "suman", "anita", formatfunc=printName2)
formatName("namita", "priya", "suman", "anita", formatfunc=printName3)