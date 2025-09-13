def greetings(choice):
    if choice == 1:
        def indianGreeting(name):
            print("Namaste", name)
        return indianGreeting
    elif choice == 2:
        japeneseGreeting = lambda name: print("Honnichiwa", name)
        return japeneseGreeting
    elif choice == 3:
        return lambda name: print("How you doing", name)
    else:
        return lambda name: print("Hello", name)


func = greetings(1)
func('Namoo')

greetings(2)('Joey')
greetings(5)('priya')

