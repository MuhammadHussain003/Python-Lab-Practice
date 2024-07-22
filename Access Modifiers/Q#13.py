class Movie:
    def __init__(self,title,director,release_year):
        self.__title=title
        self.__director=director
        self.__release_year=release_year

    def get_title(self,):
        print("Movie title",self.__title)
    def set_title(self,new_title):
        self.__title=new_title

    def get_director(self):
        print("Movie Director is",self.__director)
    def set_director(self,new_director):
        self.__director=new_director

    def get_release(self):
        print("Release date is:",self.__release_year)
    def set_release(self,new_release_year):
        self.__release_year=new_release_year


m = Movie("3 idiot","Amir Khan",2013)
m.get_title()
m.get_director()
m.get_release()
m.set_title("Punjab")
m.set_director("Salman")
m.set_release(2019)
m.get_title()
m.get_director()
m.get_release()
