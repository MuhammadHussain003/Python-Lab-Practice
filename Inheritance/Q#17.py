class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name}\n I am {self.age} year old....")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def teacher(self):
        print(f"I am teaching {self.subject} ")

class Student(Person):
    def __init__(self,name,age,StudentID,subject):
        super().__init__(name,age)
        self.subject=subject
        self.StudentID=StudentID
    def student_info(self):
        print(f"My student Id no is{self.StudentID}\n I am studying {self.subject}")




p=Person("Ali Sherwani",32)
p.info()
t=Teacher("ali haider",24,"English")
t.teacher()
s=Student("Ali Sher",23,123,"math")
s.student_info()