def heightFunc(**data):
    tallflag = 0
    shortflag = 10
    tallestStudent = 0
    shortStudent = 0
    for name in data:
        if data[name] > tallflag:
            tallflag = data[name]
            # print('max:',tallflag)
            tallestStudent = tallflag

        if data[name] < shortflag:
            shortflag = data[name]
            # print('min:',data[name])
            shortStudent = data[name]
    return tallestStudent, shortStudent

values = heightFunc(namita=4,shradha=8.5,kishor=6,joey=6.5,chandy=2)
print(values)

#birthday guest func
def birthdayGuest(*guest):
    return len(guest)

guests = birthdayGuest('monika','ross','joey','chandler','gunther','phoebe', 'rachel')
print(guests)

def inviteFunc(*guests, venue, date,time,giftoptions=""):
    totalguests = birthdayGuest(*guests)
    print('Total guest invited are: ', totalguests)
    borderchar = input('Please enter char:')

    for i in range(0,30):
        print(borderchar, end="")
    print(end="\n")
    print("U R Invited to the Birthday OF : Namita")
    print("ON: ", date, time)
    print("WHERE :", venue)

    for i in range(0,30):
        print(borderchar, end="")


inviteFunc('monika','ross','joey','chandler','gunther','phoebe', 'rachel', venue="Ashish Garden, Kothrud",
           date="16-01-2025", time="7pm")

inviteFunc('monika','ross','joey','chandler','gunther','phoebe', 'rachel', venue="Moraya Banquet Hall, Baner",
           date="16-01-2025", time="7pm")