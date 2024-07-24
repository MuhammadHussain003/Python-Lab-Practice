class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def __str__(self):
        return f" Name : {self.name}, Age : {self.age}, Address : {self.address}"
class Student(Person):
    def __init__(self,name,age,address,student_Id,grade,assigned_course):
        super().__init__(name,age,address)
        self.student_Id = student_Id
        self.grade = grade
        self.enrolled_course = []
    def __str__(self):
        return f"Student Id: {self.student_Id} { super().__init__() },Grade: {self.grade}"
class Teacher(Person):
    def __init__(self,name,age,address,employee_Id,subject,assigned_course):
        super().__init__(name,age,address)
        self.employee_Id = employee_Id
        self.subject = subject
        self.assigned_course = []
    def __str__(self):
        return f"Employee Id : {self.employee_Id} {super().__init__()} Subject : {self.subject} Assigned Course: {self.assigned_course}"
class Course:
    def __init__(self,course_name,course_code,enrolled_student):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_student = []
    def __str__(self):
        return f"Course Name: {self.course_name}, Course Code: {self.course_code} enrolled_student: {self.enrolled_student}"
class School:
    def __init__(self):
        self.student = []
        self.teacher = []
        self.courses = []
    def add_student(self,student):
        for student in self.student:
            self.student.append(student)
            print(self.student)
    def add_teacher(self,teacher):
        for teacher in self.teacher:
            self.teacher.append(teacher)
    def create_course(self,course_name,course_code):
        course = (course_code,course_name)
        self.courses.append(course)
        return course
    def assign_course_teacher(self,teacher,course):
        if teacher not in self.teacher:
            print("Teacher are not enrolled in this school....")
        if course not in self.courses:
            print("This course are not enrolled in this school syllabus")
        teacher.assigned_courses.append(course)
    def enrolled_student_in_course(self,student,course):
        if student not in self.student:
            print("This student are not enrolled in this institution ")
        if student not in course.enrolled_student:
            course.enrolled_student.append(course)
    def student_list(self):
        print(".....List of student.....")
        for student in self.student:
            print(student)
    def teacher_list(self):
        print(">>>> List of Teacher  >>>>")
        for teacher in self.teacher:
            print(teacher)
    def course_list(self):
        print(">>>>> List of Course >>>>>>")
        for course in self.courses:
            print(course)

sc = School()

s =Student("Ali",17,"House No 17 RehmanAbad RWP",1234,9,["English","Math","Physics"])
sc.add_student(s)
t = Teacher("Bilah Shahid",34,"Wah Cannt RWP","ET-100","Programming Fundamental",["Math","English","Computer"])
c = Course("Bsc IET","IEH-203",["Adil","Ali"])





