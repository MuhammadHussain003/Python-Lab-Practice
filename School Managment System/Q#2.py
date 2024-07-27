class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Student(Person):
    def __init__(self, name, age, address, student_Id, grade, enrolled_course=None):
        super().__init__(name, age, address)
        self.student_Id = student_Id
        self.grade = grade
        self.enrolled_course = enrolled_course

class Teacher(Person):
    def __init__(self, name, age, address, employee_Id, subject, assigned_course=None):
        super().__init__(name, age, address)
        self.employee_Id = employee_Id
        self.subject = subject
        self.assigned_course = assigned_course

class Course:
    def __init__(self, course_name, course_code, enrolled_students=None):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = enrolled_students

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, name, age, student_Id, address, grade, enrolled_course=None):
        student = Student(name, age, address, student_Id, grade, enrolled_course)
        self.students.append(student)
        print(f"Added Student: Name: {name}, Age: {age}, Student Id: {student_Id}, Address: {address}, Grade: {grade}, Enrolled Course: {enrolled_course}")

    def add_teacher(self, name, age, employee_Id, address, subject, assigned_course=None):
        teacher = Teacher(name, age, address, employee_Id, subject, assigned_course)
        self.teachers.append(teacher)
        print(f"Added Teacher: Name: {name}, Age: {age}, Emp-Id: {employee_Id}, Address: {address}, Subject: {subject}, Assigned Course: {assigned_course}")

    def assign_course_teacher(self, teacher, course):
        teacher.assigned_course.append(course)
        course.enrolled_students = []  # Clearing enrolled students when assigning a new teacher
        print(f"Assigned Course to Teacher: Name: {teacher.name}, Age: {teacher.age}, Emp-Id: {teacher.employee_Id}, Address: {teacher.address}, Subject: {teacher.subject}, Assigned Course: {teacher.assigned_course}")

    def enroll_student_in_course(self, student, course):
        student.enrolled_course.append(course)
        course.enrolled_students.append(student)
        print(f"Enrolled Student: Name: {student.name}, Age: {student.age}, Student Id: {student.student_Id}, Address: {student.address}, Enrolled Course: {student.enrolled_course}")


school = School()

print("\t\t\t\t********  Student  *******")
student = Student("Ali", 19, "Baltistan", 123, 13, ["BS Computer Science"])
school.add_student(student.name, student.age, student.student_Id, student.address, student.grade, student.enrolled_course)

print("\t\t\t\t*******  Teacher  *******")
teacher = Teacher("Bilal Shahid", 34, "Wah Cannt RWP", "ET-100", "Programming Fundamental", ["BS Computer Science"])
school.add_teacher(teacher.name, teacher.age, teacher.employee_Id, teacher.address, teacher.subject, teacher.assigned_course)

print("\t\t\t\t\t***** Create Course *****")
course = Course("Bs Computer Science", "BSCS-203", ["Ali"])
print(f"Created Course: Name: {course.course_name}, Code: {course.course_code}, Enrolled Students: {course.enrolled_students}")

print("\t\t\t\t\t*******  Assigned Course  *******")
school.assign_course_teacher(teacher, course)


print("\t\t\t\t\t*******  Enrolled Student In Course  *******")
school.enroll_student_in_course(student, course)
