colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']

while True:
    choice = input("Enter your fav color:")
    if choice in colors:
        print("Yes, we have this color in list")
    elif choice not in colors and choice != "quit":
        print("No, we have this color in list")
        colors.append(choice)
    elif choice == "quit":
        break
