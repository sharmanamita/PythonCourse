
list1 = [x for x in range(30)]

newlist = map(lambda x: x**3, list1)
print(list(newlist))

def getnewvaluex(x):
    return str(x)*3

print(list(map(getnewvaluex, list1)))




