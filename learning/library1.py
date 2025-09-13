from datetime import date

def calcFactoral(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

def calcSum(*args):
    total = 0
    for x in args:
        total += int(x)
    return total

def getMinorsAndAdults(personList, type):
    minors = []
    adults = []
    today = date.today()
    for record in personList:
        age = today.year - record[3].year
        if age < 18:
            minors.append(f"{record[1]}({age})")
        else:
            adults.append(f"{record[1]}({age})")

    if type == "minors":
        return minors
    else: return adults
