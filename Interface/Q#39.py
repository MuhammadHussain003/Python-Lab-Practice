from abc import  ABC,abstractmethod
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Document(Printable):
    def print(self):
        print("Print my document....")

class Photo(Printable):
    def print(self):
        print("Print  our trip photo....")
class Label(Printable):
    def print(self):
        print("Print photo with label....")
d = Document()
d.print()
p = Photo()
p.print()
l = Label()
l.print()