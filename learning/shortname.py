

nameList = ["Monika", "Chandler"]
flag = len(nameList[0])
shortestName = ""

while True:
	name = input("Please enter a name:")
	nameList.append(name)

	for name in nameList:
		print(name, len(name))
		if len(name) <= flag:
			flag = len(name)
			shortestName = name
			
	print("Short length name: ", shortestName)
	