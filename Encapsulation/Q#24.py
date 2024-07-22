class Library:
    __books=[]
    def __init__(self,books):
       self.__books = books

    def add_books(self,book):
            self.__books.append(book)
            print(f"Book in list : {self.__books}")
    def remove_books(self,book):
        if book in self.__books:
            self.__books.remove(book)
        else:
            print("Book not found in library")

    def search_book(self,book):
        if book in self.__books:
            print(f"Book {book} found in library.........")
        else:
            print(f" {book} not found in library..")

l = Library(["Math","English","Urdu","Islamiyat"])
l.add_books("Pak studies")
l.search_book("Pak studies")
