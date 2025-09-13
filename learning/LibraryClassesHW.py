class Library:
    def __init__(self, books):
        self.booksNames = books

    def getBookName(self):
        book = input("Enter the book name")
        return book

    def createBookDict(self):
        self.bookDict = {}
        for book in self.booksNames:
            copies = input("Enter the number of copies of ->" + book)
            self.bookDict[book] = int(copies)

    def showAllBooks(self):
        print("List of Books: ", self.bookDict)

    def addBook(self):
        self.booksNames.add(self.getBookName())


    def removeBook(self):
        self.booksNames.remove(self.getBookName())

    def issueBook(self):
        book = self.getBookName()
        for book in self.bookDict:
            if self.bookDict[book] != 0:
                self.bookDict[book] = self.bookDict[book] - 1
                return True
            else:
                return False
        # else:
        #     print("The book " + book + " is not in the library")
        #     return False

    def returnBook(self):
        book = self.getBookName()
        if book in self.bookDict:
            if self.bookDict[book] >= 0:
                self.bookDict[book] += 1
            else:
                print("Error!")

    def __str__(self):
        return f"The books names are: {self.bookDict}"




names = {"Data Structures & Algorithms", "Networking", "Control systems", "Basic Programming Languages"}
library = Library(names)
library.createBookDict()

print('Menu',
'1.Show',
'2.Add',
'3.Remove',
'4.Issue book',
'5.Return book',
'6.quit', sep="\n")

while True:
    choice = input('Please select above:')
    if choice == '1':
        library.showAllBooks()
    if choice == '2':
        library.addBook()
    if choice == '3':
        library.removeBook()
    if choice == '4':
        if library.issueBook():
            print("The Book issued Sucessfully!")
        else:
            print("Book is Out of Stock!")
    if choice == '5':
        library.returnBook()
    if choice == '6':
        break






