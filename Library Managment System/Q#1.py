class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed successfully!")
        else:
            print(f"{self.title} is not available.")

    def return_book(self):
        self.available = True
        print(f"{self.title} returned successfully!")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < 3:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print("You have already borrowed 3 books.")

    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.return_book()


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Available Books:")
        if book.available:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                break

    def register_member(self, member):
        self.members.append(member)
        print("Registered Members:")
        print(f"Name: {member.name}, Member ID: {member.member_id}")
    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")


library = Library()

book1 = Book("Math", " Bilal Sheikh", "123")
book2 = Book("English", " Asif Saeed", "456")

library.add_book(book1)
library.add_book(book2)

member1 = Member("Ali", "M001")
library.register_member(member1)

library.display_books()

member1.borrow_book(book1)
member1.borrow_book(book2)

library.display_books()

member1.return_book(book1)

library.display_books()

