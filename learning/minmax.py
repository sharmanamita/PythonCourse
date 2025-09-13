#Program for slicing the list and printing MIN MAX
mylist = []

fromIndex = int(input("Enter from: "))
toIndex = int(input("Enter to: "))

mylist = list(range(fromIndex, toIndex+1))

sliceI = int(input("Enter slice from: "))
sliceJ = int(input("Enter slice to: "))

while True:
	
	slicedList = mylist[sliceI:sliceJ+1]
	print("original List: ", mylist)
	print("sliced list: ", slicedList)
	
	print("Select below:", "1. The SUM of all numbers in that slice", "2. show the MAX and MIN number in that slice", "3. Quit", sep="\n")
	menu = int(input())
	
	if menu == 1:
		sum = 0
		for i in slicedList:
			sum = sum + i
		print("SUM of all numbers in that slice: ",  sum)
	elif menu == 2:
		slicedList.sort()
		print("MAX and MIN number in that slice: ", slicedList[0], slicedList[len(slicedList)-1]) 
	elif menu == 3:
		break

