from datetime import date, datetime
import calendar

#1
startDate = input("Please enter your working start date:")
start = list(map(lambda x : int(x), startDate.split("/")))
endDate = input("Please enter your working end date:")
end = list(map(lambda y : int(y), endDate.split("/")))
print(start, end)


dailywages = int(input("Enter your daily wage"))

def calcSundays(startdate, enddate):
    numOfDays = (enddate-startdate).days
    numofSundays = numOfDays//7
    print("Total working days:", numOfDays)
    print("Salary amount is:", (numOfDays-numofSundays)*dailywages)

calcSundays(date(day=start[0], month=start[1], year=start[2]),
            date(day=end[0], month=end[1], year=end[2]))

#2
month = int(input("Plese enter month:"))
numofdays = (calendar.monthrange(year=2025, month=month)[1])

healthTrackDict = {}
for day in range(1,numofdays):
    healthTrackDict.update({day: {'sleephours': 0, 'calorieIntake': 0, 'walktime': 0}})

print(healthTrackDict)

while True:
    day = int(input("Please enter one date to add data"))
    details = input("Please enter sleephours, calories, walktime:")
    data = details.split(",")

    healthTrackDict[day]['sleephours'] = int(data[0])
    healthTrackDict[day]['calorieIntake'] = int(data[1])
    healthTrackDict[day]['walktime'] = int(data[2])

    print("Menu", "1.Total walk done in this month","2.Total sleep", "3.Total calories", "4.Quit", sep="\n")
    choice = int(input("Plese select above:"))

    if choice == 1:
        totalWalk = 0
        for day in healthTrackDict:
            totalWalk =  totalWalk + healthTrackDict[day]['walktime']
        print("Total Walktime for month is ", totalWalk)
    elif choice == 2:
        totalSleep = 0
        for day in healthTrackDict:
            totalSleep = totalSleep + healthTrackDict[day]['sleephours']
        print("Total Sleep for month is ", totalSleep)
    elif choice == 3:
        totalCalories = 0
        for day in healthTrackDict:
            totalCalories = totalCalories + healthTrackDict[day]['calorieIntake']
        print("Total Calories for month is ", totalCalories)
    elif choice == 4:
        break




#3
students=["namita sharma", "priya pawar", "anita shinde", "vaishanavi patil", "somak kanjilal"]
titlelist = list(map(lambda x : x.split(" ")[0][0].upper()+x.split(" ")[0][1:] + " "+
                                x.split(" ")[1][0].upper()+x.split(" ")[1][1:] , students))
print("Titled List:",titlelist)

#4
dairylist = [
{ "pname" : "cheese" , "expirydate":datetime(year=2020,month=11,day=1) },
{ "pname" : "butter" , "expirydate":datetime(year=2025,month=5,day=1) },
{ "pname" : "jam" , "expirydate":datetime(year=2025,month=11,day=1) },
{ "pname" : "bread" , "expirydate":datetime(year=2025,month=1,day=29) },
{ "pname" : "milk" , "expirydate":datetime(year=2025,month=1,day=23) },
{ "pname" : "juice" , "expirydate":datetime(year=2025,month=6,day=6) },
{ "pname" : "yogurt" , "expirydate":datetime(year=2025,month=1,day=20) }]

newlist = filter(lambda product: (product['expirydate'] >= datetime.now()), dairylist)
print("Org Dairylist:",dairylist)
print("Modified list:",list(newlist))

#6
dateslist = [date(year=2025, month=1, day=26), date(year=2025, month=1, day=27), date(year=2025, month=1, day=28),
             date(year=2025, month=1, day=29), date(year=2025, month=1, day=30), date(year=2025, month=1, day=31)]

dayofdates = [(x.strftime('%d/%b/%y'), x.strftime('%A')) for x in dateslist ]
print("Tuple of date and week day:", dayofdates)