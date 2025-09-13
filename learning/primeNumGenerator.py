
def printPrimeNums(start, end):
    for x in range(start,end):
        isprime =True
        for y in range(2,x):
            if x%y ==0:
                isprime = False
                break
            continue
        if isprime:
            # print(x, end=",")
            yield x
            continue

a = printPrimeNums(2,100)
print(next(a))
print(next(a))
