class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Bookstore:
    books=[]
    def __init__(self,books):
        self.books = books

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added '{title}' by {author} to the bookstore.")

    def find_books_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            print(f"Books found by {author}:")
            for book in found_books:
                print(f"- {book.title}")
        else:
            print(f"No books found by {author} in the bookstore.")


obj=Bookstore(["crisis","by hasmat kamal"])
obj.add_book()