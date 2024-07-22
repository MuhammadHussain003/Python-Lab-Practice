class User:

    def __init__(self,__user_name,__password):
        self.__user_name = __user_name
        self.__password = __password

    def get_username(self):
        print("user name is:",self.__user_name)
        print("user password is: ",self.__password)

    def change_username(self,new_username):
        self.__user_name = new_username
        print("New user name is",self.__user_name)

    def change_password(self,current_password,new_password):
        if self.__password == current_password:
            self.__password=new_password
            print("Password changed successfully")
        else:
            print("Invalid password try again!")

user = User("Saleem1","saleem123")
user.get_username()
user.change_password("saleem123","saleem321")
user.get_username()