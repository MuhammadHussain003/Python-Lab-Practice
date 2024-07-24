class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_limit = 3

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{self.book}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{self.books}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member}' registered.")

    def borrow_book(self, member, book_title):
        if member in self.members:
            if len(member.borrowed_books) < self.borrow_limit:
                for book in self.books:
                    if book.title == book_title and book.available:
                        member.borrowed_books.append(book)
                        print(f"Book '{book.title}' borrowed by {member.name}.")
                print(f"Book '{book_title}' is not available.")
            else:
                print(f"Member {member.name} has reached the maximum borrow limit.")
        else:
            print(f"Member '{member.name}' is not registered.")

    def return_book(self, member, book_title):
        for book in member.borrowed_books:
            if book.title == book_title:
                member.borrowed_books.remove(book)
                book.available = True
                print(f"Book '{book.title}' returned by {member.name}.")
                return
        print(f"Member '{member.name}' did not borrow '{book_title}'.")

    def print_books(self):
        print("Books available in the library:")
        for book in self.books:
            print(f"- {book}")

    def print_members(self):
        print("Members registered in the library:")
        for member in self.members:
            print(f"- {member}")

l = Library()
l.add_book(["Current affair","Politics in Pakistan"])
l.register_member(["asdfas","jaffar","hassan"])
l.remove_book("Current affair")



