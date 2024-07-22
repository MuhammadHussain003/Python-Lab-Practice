class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def find_books_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
                print(found_books)



obj = Bookstore()
obj.add_book("Book1", "Author1")
obj.add_book("Book2", "Author2")
author_to_find = "Author1"
books_by_author = obj.find_books_by_author(author_to_find)

