class Costumer:
    def __init__(self,name,email,phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

    def get_name(self):
        print(f" My name : {self.__name}")
    def set_name(self,new_name):
        self.__name=new_name
        print(f"My new|nick name is: ",self.__name)

    def get_email(self):
        print(f" My email is : {self.__email}")

    def set_email(self, new_email):
        self.__email = new_email
        print(f"My new email  is: ", self.__email)

    def get_phone_number(self):
        print(f"My phone number is {self.__phone_number}")

    def set_phone_number(self, new_phone_number):
       self.__phone_number = new_phone_number
       print(f"My new phone number is {self.__phone_number}")


c = Costumer("Hassan","imhussain@gmail.com",922312321)
c.get_name()
c.get_email()
c.get_phone_number()
c.set_name("Khurram")
c.set_email("imuhan12@gmail.com")
c.set_phone_number(92345678)