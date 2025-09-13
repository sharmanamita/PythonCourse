symbol=''
lines=0


symbol = input('Please enter symbol: ')
lines = int(input('Enter number of lines: '))

for x in range(lines, 0, -1):
	for y in range(x):
		print(symbol, end=" ")
	print("")
for x in range(2, lines+1):
	for y in range(x):
		print(symbol, end=" ")
	print("")

