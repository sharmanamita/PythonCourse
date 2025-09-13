#Program for appending the list and printing duplicates

mylist = [1, 2, 5, 5]

while True:
	
	print("Select below:", "1. Append to list", "2.Show list", "3.SLICE list --- Enter index(from,to)" , "4.Quit", sep="\n")
	menu = int(input())
	
	if menu == 1:
		item = int(input("Enter value: "))
		mylist.append(item)
	elif menu == 2:
		print("original List: ", mylist)
	elif menu == 3:
		sliceI = int(input("Enter slice from:"))
		sliceJ = int(input("Enter slice to:"))
		slicedList = mylist[sliceI:sliceJ+1]
		
		print("sliced list: ", slicedList)
		
		print("Duplicated values:")
		for i in range(0, len(slicedList)):
			for j in range(i+1, len(slicedList)):
				if slicedList[i] == slicedList[j]:
					print(slicedList[j])
	elif menu ==4:
		break