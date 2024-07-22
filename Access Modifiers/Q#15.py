class Book:
    title=""
    author=""
    ISBN=0
    def __init__(self,title,author,ISBN):
        self.title=title
        self.author=author
        self.ISBN=ISBN

class Library:
    __books=[]
    def add(self,title,author,ISBN):
        book=Book(title,author,ISBN)
        self.__books.append(book)

    def remove_ISBN(self, author):
        flag = None
        for index in range(0, len(self.__books)):
            if (self.__books[index].author == author):
                flag=self.__books[index].author
                self.__books.pop(index)
            else:
                flag=False

        if(flag):
            print(f"Book {flag} has been remove")
        else:
            print("Book was not found in the list")
    def display(self,):
        for book in self.__books:
            print(f"""
                   *************Books Info************* 
                       title  :{book.title}
                       author :{book.author}
                       ISBN   :{book.ISBN}
                          """)




    def search(self,author):
        flag=False
        for book in self.__books:
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
obj.remove_ISBN("shazil")
obj.search("shaheer")
obj.search("shazil")
obj.display()

