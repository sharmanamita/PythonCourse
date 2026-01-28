# List - Muttable, ordered, allows duplicates

myList = [x for x in range(1,11)]
myList.append(11)
myList.append(11) # duplicates allowed
myList.append(75)
myList.append(13)
myList.append('namita')

# myList.pop() #pops last element
myList.remove(5) # removes (based on value) first occurrence of 1
print("List elements:", myList)

# set - unordered, mutable, no duplicates allowed
mySet = { x for x in range(2, 11)}
mySet.add(11)
mySet.add(5)
mySet.pop() # pops first element
mySet.add(1)
mySet.add(75)
mySet.add(12)
mySet.add('namita')
mySet.remove(7) # removes (based on value) first occurrence of 1
print("Set before adding duplicates:", mySet, end="\n\n")

# tuple - immutable, ordered, 
myTuple = (x for x in range(1,11))
print("Tuple elements:", myTuple) # as this wont print values, it prints generator object
# myTuple[2] = 25 # throws error as tuples are immutable
# myTuple.add(50) # throws error as tuples are immutable

mytuple2 = ("Namita", "Pune", 19, 1997, "Namita", "Pune")
print("Tuple elements:", mytuple2)

# dictionry - mutable, key-value pairs, no duplicate key allowed
myDict = {
    "name" : "Namita",
    "age" : 25,
    "city" : "Pune"
}
print("Dictionary elements:", myDict.get("name"), myDict['age'], myDict['city'])

# converting tuple to list to remove duplicates
print("Tuple to list conversion to remove duplicates:", list(mytuple2))

#converting tuple to set to remove duplicates
print("Tuple to set conversion to remove duplicates:", set(mytuple2))

#converting tuple to dictionary to remove duplicates
print("Tuple to dict conversion to remove duplicates:", dict.fromkeys(mytuple2))