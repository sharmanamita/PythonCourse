
f = open('./readfile.txt', 'r')



f.seek(0) #resetting the poistion of file pointer to 0
print("printing in for...")
lines = f.readlines()

for line in lines:
    print(line)
f.close()

# write into file
f1 = open("readfile.txt", 'w')

f1.write("Tit for tat")

