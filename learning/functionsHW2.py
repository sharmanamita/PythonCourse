def calcVolume(height=2, width=4, base=1):
    return base * height * width

volume = calcVolume()

while True:
    print("1.Height",
        "2.Base",
        "3.Width",
        "4.Base and height",
        "5.Base and width",
        "6.Width and height",
        "7.All 3",
        "8.None",
        "9.Quit",sep="\n")
    menu = int(input("Enter your choice: "))
    if menu == 1:
        h = int(input("Height: "))
        print('Volume:', calcVolume(height=h))
    if menu == 2:
        b = int(input("Base: "))
        print('Volume:', calcVolume(base=b))
    if menu == 3:
        w = int(input("Width: "))
        print('Volume:', calcVolume(width=w))
    if menu == 4:
        d = input("Base and height: ")
        data=d.split(",")
        print('Volume:', calcVolume(base=int(data[0]), height=int(data[1])))
    if menu == 5:
        x = input("Base and width: ")
        data = x.split(",")
        print('Volume:', calcVolume(base=int(data[0]), width=int(data[1])))
    if menu == 6:
        y = input("Width and height: ")
        data = y.split(",")
        print('Volume:', calcVolume(width=int(data[0]), height=int(data[1])))
    if menu == 7:
        y = input("Width and height and base: ")
        data = y.split(",")
        print('Volume:', calcVolume(width=int(data[0]), height=int(data[1]), base=int(data[2])))
    if menu == 8:
        print(calcVolume())
    if menu == 9:
        break