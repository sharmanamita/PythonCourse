x=int(input("Enter a value"))

if x<100:
	y = x%7
	if y == 0:
			print("x is divisible by 7")
	else :
			print("x is not divisible by 7")

else: 
	print("x is greater than 100")