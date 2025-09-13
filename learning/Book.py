class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"



obj1 = Book("Python Learning", "Prachi", 500)
obj2 = Book("Javascript Learning", "Namita", 450)

print(obj1, obj2)


class Magzine(Book):
    def __init__(self, title, author, pages, frequency):
        super().__init__(title, author, pages)
        self.frequency = frequency

    def __str__(self):
        return f"{super().__str__()} and {self.frequency}"


mag1 = Magzine("Cpp Learning", "Suman", 560, 'Monthly')
print(mag1)