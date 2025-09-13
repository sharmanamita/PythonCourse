#Program for print prime numbers

i = int(input("Enter from:"))
j = int(input("Enter to:"))
flag = 0
list = []

print("Prime numbers are:")
for num in range(i, j+1):
	for i in range(2, num):
		if num%i == 0:
			flag = 1
			break
		else:
			flag = 0
			
	if flag ==0:
		list.append(num)
		
print(list)
	