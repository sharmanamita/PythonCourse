import threading
import time

def facGen(num):
    for x in range(1, num+1):
        y = calcFactorial(x)
        yield y

def calcFactorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print(fact)

def myThread(num):
    gen = facGen(num)
    while True:
        try:
            next(gen)
            time.sleep(2)
        except (StopIteration) as e:
            break




def printTable(tblfrom, tblto, tblupto):
    file = open("./tables.txt", 'a')

    for num in range(tblfrom, tblto+1):
        for x in range(1, tblupto+1):
            content = f"{num} x {x} = {num*x}"
            file.write(content+"\n")
            # print("num:", num, "x:", x)
        file.write("---------------------"+"\n")
        print(f"Table for {num} is added")
        time.sleep(2)
        continue

    file.close()


num = int(input("Enter number to see factorial"))
thread1 = threading.Thread(target=myThread, kwargs={'num': num})
thread1.start()

tblfrom = int(input("Enter table range from:"))
tblto = int(input("Enter table range to:"))
tblupto = int(input("Enter table range upto:"))
thread2 = threading.Thread(target=printTable, kwargs={'tblfrom':tblfrom, 'tblto':tblto, 'tblupto': tblupto})
thread2.start()

thread1.join()
thread2.join()

print("THANK YOU!")

