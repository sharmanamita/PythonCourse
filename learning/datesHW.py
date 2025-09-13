from datetime import date

birthdate = input("Enter birth date (dd/mm/yyyy): ")
d = birthdate.split("/")

userdate = date(day=int(d[0]), month=int(d[1]), year=int(d[2]))

d1 = date(day=int(d[0]), month=int(d[1]), year=int(d[2]))
week = d1.isocalendar().week
day = d1.weekday()

if week == 2 and day == 5:
    print("This date is 2nd Saturday Holiday")
elif week == 4 and day == 5:
    print("This date is 4th Saturday Holiday")
elif day == 6:
    print("Today is Sunday")
else:
    print("No Holiday")


