import threading

def job1():
    x = 0
    while x < 10:
        print("Job 1", threading.current_thread().name)
        x +=1

def job2(message):
    for x in range(10):
        print(message)
    job3("prachi")

def job3(msg):
    print(msg)

#main thread
print(threading.current_thread().name)

pathofexcution = job1
thread1 = threading.Thread(target=pathofexcution)
# thread1.start()

thread2 = threading.Thread(target=job2, kwargs={'message': "Good Morning"})
# thread2.start()

thread1.start()
thread2.start()

thread1.join()
thread2.join()# to make threads wait until another threads are not done

print("Good Bye!!")

# for x in range(30):
#     print(threading.current_thread().name)


