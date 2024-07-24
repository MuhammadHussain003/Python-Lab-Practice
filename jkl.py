class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Initially, book is available

    def book_detail(self):
        print( f"{self.title} by {self.author}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def member_detail(self):
        print( f"Member: {self.name} (ID: {self.member_id})")


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_limit = 3  # Maximum number of books a member can borrow

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print("Book not found in the library.")

    def register_member(self, name, member_id):
        new_member = Member(name, member_id)
        self.members.append(new_member)
        print(f"Member '{name}' registered with ID: {member_id}")

    def borrow_book(self, member_id, isbn):
        member = self.find_member_by_id(member_id)
        if member is None:
            print("Member not found.")

        if len(member.borrowed_books) >= self.borrow_limit:
            print("You have reached the maximum borrow limit.")

        book = self.find_book_by_isbn(isbn)
        if book is None:
            print("Book not found in the library.")
            return

        if not book.available:
            print(f"Book '{book.title}' is currently not available.")
            return

        member.borrowed_books.append(book)
        book.available = False
        print(f"Book '{book.title}' borrowed by {member.name}.")

    def return_book(self, member_id, isbn):
        member = self.find_member_by_id(member_id)
        if member is None:
            print("Member not found.")
            return

        for book in member.borrowed_books:
            if book.isbn == isbn:
                member.borrowed_books.remove(book)
                book.available = True
                print(f"Book '{book.title}' returned by {member.name}.")
                return

        print("You have not borrowed this book.")

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def print_books(self):
        print("\nLibrary Catalog:")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                status = "Available" if book.available else "Not Available"
                print(f"{book.title} by {book.author} [{book.isbn}] - {status}")

    def print_members(self):
        print("\nLibrary Members:")
        if not self.members:
            print("No members in the library.")
        else:
            for member in self.members:
                print(f"{member.name} (ID: {member.member_id})")



library = Library()


library.add_book("Current Affair", "Khalil-ur-Rahman", "1234")
library.add_book("Politics ", " Anwar Masud", "5678")

library.register_member("Ali", 101)
library.register_member("Babar", 102)


library.borrow_book(101, "1234")
library.borrow_book(102, "5678")



library.print_books()
library.print_members()

library.return_book(101, "123")

library.print_books()
