class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id, courses):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = courses
        self.grades = {}

    def add_grade(self, course, grade):

        self.grades[course]=grade

    def calculate_gpa(self):

        return sum(self.grades.values()) / len(self.grades)

    def result(self):
        print(f"Student ID: {self.student_id}")
        print("Courses:")
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
        print(f"GPA: {self.calculate_gpa()}")


person = Person("Ali ", 19)
person.display()

student = Student("Ali",19,12345, ["Math", "Science", "English"])
student.add_grade("Math", 90)
student.add_grade("Science", 85)
student.result()