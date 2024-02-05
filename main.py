class Student:
    school = "XYZ University"
    location = "City"
    country = "Country"

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        print(f"Student {self.name}, {self.age} years old, studying {self.major} at {self.school}.")

student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 22, "Physics")
student3 = Student("Charlie", 21, "Engineering")

student1.display_info()
student2.display_info()
student3.display_info()

print("\n")

class Book:
    language = "English"
    genre = "Fiction"
    publication_year = "2022"

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"The book '{self.title}' by {self.author} has {self.pages} pages and belongs to the {self.genre} genre.")

book1 = Book("The Adventure Begins", "John Doe", 300)
book2 = Book("Mystery of the Shadows", "Jane Smith", 250)
book3 = Book("Science Fiction Odyssey", "Alan Johnson", 400)

book1.display_info()
book2.display_info()
book3.display_info()
