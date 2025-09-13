
username = input(print('Please enter your name:'))
print("Menu",
 "1 - show string in upper using caps",
 "2 - show string in lower using lows",
 "3 - show string in upper using title",
 "4. quit", sep="\n" )
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        caps = (lambda name: name.upper())(username)
        print(caps)
    elif choice == 2:
        lows = (lambda name: name.lower())(username)
        print(lows)
    elif choice == 3:
        title = (lambda name: name[0:1].upper() + name[1:].lower())(username)
        print(title)
    elif choice == 4:
        break