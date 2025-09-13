def my_gen():

    n = 1

    print("First iteration")

    yield n

    n += 1

    print("Second iteration")

    yield n

    n += 1

    print("third iteration")

    yield n


a = my_gen() #always take it in var for new values
print(next(a))
print(next(a))
print(next(a))




