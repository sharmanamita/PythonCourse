x=float(input("Enter a value: "))

if x>=60 and x<=70 :
	print("FIRST CLASS")
elif x>=50 and x<=60 :
	print("SECOND CLASS")
elif x>=40 and x<=50 :
	print("THIRD CLASS")
elif x<40:
	print("FAIL")
elif x>70:
	print("DISTINCTION")


x = 4
x+=2
x*=3
x/=2
print(x)

y = 13/3 #it will return float number
y = y//3 # called as floor division to round of the value
print (y)

x=2
z = x**3#cube
print(z)

x = [10,20,30]
y = [10,20,30]

print(x is y) # comparing with reference
print(x == y) # comparing with values

print(x is not y)
print(x != y)

#IN / NOT IN
x  = [10,20,30] #list
print(10 in x)
print(40 not in x)

x = {"name":"namita", "age":25} #dict
print('name' in x)

x = (25, "xyz", 45.5) #tuple
print(45 not in x)
print(25 in x)

x = "olympics"
print("oly" in x)
print("mp3" in x)

x=6
print("xor", x^2)
print("right shift", x<<1)
print("left shift", x>>1)