from datetime import date, datetime, timedelta

while True:
    print("Menu",
          "1. Day after adding number of days - show the date and weekday",
          "2. Day before number of days - show date and weekday",
          "3. Quit", sep="\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        days = int(input("Enter the number of days: "))
        d1 = datetime.now()
        print(d1 + timedelta(days=+days))
    elif choice == 2:
        days = int(input("Enter the number of days: "))
        d2 = datetime.now()
        print(d2 + timedelta(days=-days))
    else:
        break