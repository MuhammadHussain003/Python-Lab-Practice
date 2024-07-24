class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        pass
class Teacher(Person):
    def __init__(self,name):
        super().__init__(name)
    def introduce(self):
        print(f"My name is  {self.name}.I am a Teacher ")

class Student(Person):
    def __init__(self,name):
        super().__init__(name)
    def introduce(self):
        print(f"My name is  {self.name}. I am a student")


t = Teacher("Hassan Niazi")
s = Student("Attaullah")
t.introduce()
s.introduce()