class Book:
    def __init__(self,title,author,ISBN):
        self.title=[]
        self.author=[]
        self.ISBN=[]
    def book(self,title,author,ISBN):
        pass


class Library:
    books=[]
    def add(self,title,author,ISBN):
        book=Book(title,author,ISBN)
        self.books.append(book)

    def remove_ISBN(self, ISBN):

        for index in range(0, len(self.books)):
            if (self.books[index].ISBN == ISBN):
                self.books.pop(index)
                print("Book has been remove")

    def display(self,):
        for book in self.books:
            print(f"""
                   *************Books Info************* 
                       title  :{book.title}
                       author :{book.author}
                       ISBN   :{book.ISBN}
                          """)




    def search(self,author):
        flag=False
        for book in self.books:
            if (book.author==author):
                flag=True
                break
            else:
                flag=False

        if (flag):
            print("Book found")
        else:
            print("Book not found")





obj=Library()
obj.add("Book1","shaheer",12321)
obj.add("Book2","shazil",43452)
obj.display()
obj.search("shaheer")

