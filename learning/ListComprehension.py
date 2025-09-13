mylist = [x for x in range(10)]

print(mylist)


#traditional way
# list =[]
# for x in range(11,21):
#     list.append(x**2)
# print(list)

#list comprehension
squres = [x**2 for x in range(11,21)]
print(squres)

oddlist = [x for x in range(1, 30,2)]
print(oddlist)

colors = ['red', 'green', 'blue', 'yellow']
extendedlist = [x.upper()[0:2] for x in colors]
print(extendedlist)

divby3 = [x for x in oddlist if x%3 == 0]
print(divby3)

#create tuplelist uch as its has color and its length
tupList = [ (x, len(x)) for x in colors]
print(tupList)

#create list of dict where names are uname and len as pwd
names = ['namita', 'suman', 'mew']
dictlist = [{x,len(x)} for x in names]
print(dictlist)

#create from 2D array
numlist = [[10,20,30], [40,50,60], [70,80,90]]
allnumlist = [num for x in numlist for num in x]
print(allnumlist)


#nesting for loops
list1 = ['s1', 's2', 's3']
list2 = ['s3', 's4', 's5']
list3 = ['s5', 's6', 's7']

#[('s1', 's3', 's5'), ('s1', 's3', 's6'), ('s1', 's3', 's7'), ('s1', 's4', 's5'), ('s1', 's4', 's6'), ('s1', 's4', 's7'),
# ('s1', 's5', 's5'), ('s1', 's5', 's6'), ('s1', 's5', 's7'), ('s2', 's3', 's5'), ('s2', 's3', 's6'), ('s2', 's3', 's7'),
# ('s2', 's4', 's5'), ('s2', 's4', 's6'), ('s2', 's4', 's7'), ('s2', 's5', 's5'), ('s2', 's5', 's6'), ('s2', 's5', 's7')]

resultlist = [(x,y, z) for x in list1 if x!='s3' for y in list2 if x!=y for z in list3]
print(resultlist)

