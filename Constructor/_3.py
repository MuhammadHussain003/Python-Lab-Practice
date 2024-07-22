class Course:
    e_student=[]
    def __init__(self,c_name,c_code,e_student):
        self.c_name=c_name
        self.c_code=c_code
        self.e_student=e_student

    def display(self):
        print(f"Course name is : {self.c_name}")
        print(f"Course code is : {self.c_code}")
        print(f"Enrolled student is : {self.e_student}")

obj=Course("English","IEH-123",["Ali","Shafat","Hamza"])
obj.display()