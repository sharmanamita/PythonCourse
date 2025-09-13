from datetime import date, datetime, timedelta

birthdate = input("Enter birth date: ")
d = birthdate.split("/")

d1 = date(year=int(d[0]), day=int(d[1]), month=int(d[2]))
print(d1.weekday())
print(d1.strftime('%A'))

d2 = date(year=2025, day=int(d[1]), month=int(d[2]))
print("This year your birth date will be on: ", d2.strftime('%A'))

# print(d.strftime('%d/%b/%y'))
# print(d.strftime('%d/%b/%Y'))

# today = datetime.now()

# print(today + timedelta(days=-15))
