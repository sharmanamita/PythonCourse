x=0
limit=-1
numList = []
sum = 0

while x != limit:
	x=int(input('Enter a value: '))
	#print(numList, x)
	if x == limit:
		break
	else:
		numList.append(x)

while True:
	print('Please select a menu:', '1.Show coma separated list' , 
	'2.Show list one below the other', '3.Show sum of all numbers in the list', '4.Quit', sep="\n")
	menuNum = int(input())
	
	if menuNum == 1:
		index = 0
		for i in numList:
			index = index +1
			if len(numList)-1 == index:
				print(i)
			else:
				print(i, end=",")
		
	elif menuNum == 2:
		for i in numList:
			print(i)
	
	elif menuNum == 3:
		for i in numList:
			sum = sum + i
		print('Sum of the list is ', sum)
		
	elif menuNum == 4:
		break
	