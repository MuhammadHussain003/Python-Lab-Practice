class Book:

    def __init__(self,title,author,ISBN,availability_status):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability_status = True
class Member:

    def __init__(self,name,member_Id,borrow_book):

        self.name = name
        self.member_Id = member_Id
        self.borrowed_book = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_limit = 3

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{self.members}' registered.")

    def borrow_book(self, member, book_title):
        if member in self.members:
            if len(member.borrowed_book) < self.borrow_limit:
                for book in self.books:
                    if book.title == book_title and book.available:
                        member.borrow_book.append(book)
                        print(f"Book '{book.title}' borrowed by {member}.")

                    print(f"Book '{book_title}' is not available.")
            else:
                print(f"Member {member} has reached the maximum borrow limit.")
        else:
            print(f"Member '{member}' is not registered.")


l = Library()
l.register_member(["hassan"])
l.add_book("English")
l.borrow_book("hassan","English")