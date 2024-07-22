class Student:
    def __init__(self,name,student_Id,GPA):
        self.__name = name
        self.__student_id = student_Id
        self.__GPA = GPA

    def get_name(self):
        print(f" Student Name : {self.__name}")
    def set_name(self,new_name):
        self.__name=new_name
        print(f"Student new name is: ",self.__name)

    def get_S_Id(self):
        print(f" Student Id is : {self.__student_id}")

    def set_s_Id(self, new_Id):
        self.__student_id = new_Id
        print(f"Student new Id is: ", self.__student_id)

    def get_gpa(self):
        if 0<=self.__GPA<=4:
         print(f" {self.__name} got : {self.__GPA} GPA")
        else:
            print("Invalid GPA enter GPA in between 0 to 4")

    def set_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:
          self.__GPA = new_gpa
          print(f"Student new gpa is: ", self.__GPA,"GPA")
        else:
            print("Invalid GPA enter GPA in between 0.0 to 4.0")

s=Student("Altaf Hussain",345,3.7)
s.get_name()
s.get_S_Id()
s.get_gpa()
s.set_name("Sheikh Hassan")
s.set_s_Id(456)
s.set_gpa(3.7)