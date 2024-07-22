class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})
        print(f"Added book '{title}' by {author}")

    def find_books_by_author(self,author):
        for book in self.books:
            if (book.author==author):
                print(f"{book} author was {author}")
                break
            else:
                print("author not found")

bookstore = Bookstore()

bookstore.add_book("The Great", "Scott")
bookstore.add_book("Pride", "Austen")

bookstore.find_books_by_author("Austen")
