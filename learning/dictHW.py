weekdays = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

# while True:
choice = int(input('Please enter value between 1-7:'))
print(weekdays[choice])

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

dateInput = input('Please enter day,month & year:')
date = dateInput.split(',')

while True:
    print("1. Dd-mmm-yyyy",
          "2. Full Monthname , dd -yyyy",
          "3. Dd/mm/yyyy",
          "4. quit", sep='\n')
    choice2 = int(input('Select below format:'))
    if choice2 == 1:
        month = (months[int(date[1])])
        print(date[0], "-", month[0:3], "-", date[2])

    elif choice2 == 2:
        print(months[int(date[1])], " ", date[0], "-", date[2])

    elif choice2 == 3:
        print(date[0], "/", date[1], "/", date[2])

    elif choice2 == 4:
        break