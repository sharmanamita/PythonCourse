
mylist = [10,20,30]

iterator = iter(mylist)

try:
    print(next(iterator))
    print("do something")
    print("do something later")
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except(StopIteration) as e:
    print("Cannot proceed further", e)