# for x in range(200):
#     for y in str(x):
#         if y=='7':
#             print(x)

# list = [x for x in range(200) for y in str(x) if y == '7' ]
list = [x for x in range(200) if '7' in str(x)]
print("List of content 7:", list)

# size1 = int(input('Enter size of list1 : '))
# size2 = int(input('Enter size of list2 : '))

list1 = [ 10,20,30,44,55,19 ]
list2 =[ 10,55,100,134 ]

commanlist = [x for x in list1 for y in list2 if x == y]
print("Common List:", commanlist)
uncommanlist = [num for sublist in list(set([list1, list2])) for num in sublist]
print("Uncommon List:", uncommanlist)

inputstring = input("Enter a string: ")
nonvowelList = [char for char in inputstring.lower() if char != ' ' and char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u']
print(nonvowelList)
