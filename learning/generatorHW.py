import random

#1
quoteDict = {
    0 : "Where there is a will there is a way ",
    1: "Be the reason of someone's happiness",
    2: "Turn your wounds into wisdom",
    # 3: "Make most of present adn future will be brighter",
    # 4: "The purpose of our life is to be happy",
    # 5: "Don't giveup until you're proud",
    # 6: "Don't read your book backwards",
    # 7: "If you change nothing, nothing will be changed"
}

def quoteGen():
    for x in quoteDict:
        yield quoteDict[x]


def menu():
    quotegen = quoteGen()
    x = -1
    while True:
        print("Menu",
              "1. Show all quotes",
              "2. Add a new quote",
              "3. Get the next quote",
              "4. Quit", sep="\n")
        choice = int(input("Enter select:"))

        if choice == 1:
            for x in quoteDict:
                print(x, quoteDict[x])
        elif choice == 2:
            newquote = input("Please new Quote:")
            print(len(quoteDict)+1, newquote)
            quoteDict.update({len(quoteDict)+1: newquote })
        elif choice == 3:
            x +=1
            try:
                print(next(quotegen))
            except (StopIteration, RuntimeError):
                quotegen = quoteGen()
                print("Restarting the quotelist")
                print(next(quotegen))
        elif choice == 4:
            break

menu()

#2
n = int(input("Please enter number range from 1 to n:"))
def cubeNumbers():
    for x in range(1,n):
        yield x**3
        # print(x**3)
        continue

cubes = cubeNumbers()
print(next(cubes))
print(next(cubes))
print(next(cubes))


#3

def randomGen():
    while True:
        num = random.randint(1, 10)
        yield num

def pattern(lines):
    choice = input("Do you want to see the pattern y/n:")

    if choice == 'y':
        for x in range(lines, 0, -1):
            for y in range(x):
                print('*', end=" ")
            print("")
        for x in range(2, lines + 1):
            for y in range(x):
                print('*', end=" ")
            print("")
    else:
        print(lines)



patt = randomGen()
pattern(next(patt))
pattern(next(patt))
pattern(next(patt))

#4
def fibSeries():
    y1, y2 = 0, 1
    value = y1+y2
    for x in range(3,10):
        yield value
        y1 = y2
        y2 = value
        value = y1+y2
        continue

fibonacci = fibSeries()
while True:
    try:
        choice = input("Do you need next fibonacci number? y/n:")
        if choice == 'y':
            print("next number from fibonacci series is:", next(fibonacci))
        else:
            break
    except (StopIteration) as e:
        fibonacci = fibSeries()


