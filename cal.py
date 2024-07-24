class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

class Student(Person):
    def __init__(self, name, age, address, student_id, grade):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grade = grade
        self.enrolled_courses = []

    def __str__(self):
        return f"Student ID: {self.student_id}, {super().__str__()}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
        self.assigned_courses = []

    def __str__(self):
        return f"Employee ID: {self.employee_id}, {super().__str__()}, Subject: {self.subject}"

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = []

    def __str__(self):
        return f"Course: {self.course_name} ({self.course_code}), Students enrolled: {len(self.enrolled_students)}"

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def create_course(self, course_name, course_code):
        course = Course(course_name, course_code)
        self.courses.append(course)
        return course

    def assign_teacher_to_course(self, teacher, course):
        if teacher not in self.teachers:
            print(f"Error: Teacher {teacher.name} is not in the school.")

        if course not in self.courses:
            print(f"Error: Course {course.course_name} ({course.course_code}) does not exist in the school.")

        teacher.assigned_courses.append(course)
    def enroll_student_in_course(self, student, course):
        if student not in self.students:
            print(f"Error: Student {student.name} is not in the school.")

        if course not in self.courses:
            print(f"Error: Course {course.course_name} ({course.course_code}) does not exist in the school.")
        if student not in course.enrolled_students:
            course.enrolled_students.append(student)
            # student.enrolled_courses.append(course)

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student)

    def list_teachers(self):
        print("List of teachers:")
        for teacher in self.teachers:
            print(teacher)

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course)


school = School()


student1 = Student("Ali", 17, "House No:14,Sadiq abad RWP", "S001", 9)
student2 = Student("Babar", 16, "House No:18,Rehmanabad RWP", "S002", 10)
school.add_student(student1)
school.add_student(student2)

teacher1 = Teacher("Mr. Johnson", 35, "789 Pine St", "T001", "Math")
teacher2 = Teacher("Ms. Smith", 40, "987 Cedar St", "T002", "Science")
school.add_teacher(teacher1)
school.add_teacher(teacher2)


math_course = school.create_course("Mathematics", "MATH101")
science_course = school.create_course("Science", "SCI101")


school.assign_teacher_to_course(teacher1, math_course)
school.assign_teacher_to_course(teacher2, science_course)


school.enroll_student_in_course(student1, math_course)
school.enroll_student_in_course(student2, science_course)


school.list_students()
school.list_teachers()
school.list_courses()
