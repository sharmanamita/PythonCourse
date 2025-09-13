from PyLibraries.stringManipulators import reverseString as getReverseStr
from PyLibraries.stringManipulators import isStrPalindrome as panlindrome
from PyLibraries.stringManipulators import changeStr as modifyStr


while True:
    print("Menu", "1. rev", "2. palidrome", "3. nameInsert", "4. quit", sep="\n" )
    menu = int(input("Please select above:"))

    if menu == 1:
        name = str(input("Enter your a string:"))
        print(getReverseStr(name))
    elif menu == 2:
        name = str(input("Enter your a string:"))
        if(panlindrome(name)):
            print("String is panlindrome")
        else:
            print("String is not panlindrome")
    elif menu == 3:
        print(modifyStr())
    elif menu == 4:
        break

