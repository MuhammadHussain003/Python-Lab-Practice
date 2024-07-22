class Employee:
    def __init__(self,Employe_name,Employe_Id):
        self.Employee_name=Employe_name
        self.Employee_Id=Employe_Id
    def e_detail(self):
        print(f"""
               Employee Name is:{self.Employee_name}
               Employee ID is  :{self.Employee_Id}
""")

class Manager(Employee):
    def __init__(self,Employe_name,Employe_Id,Designation):
        super().__init__(Employe_name,Employe_Id)
        self.Designation=Designation
    def m_detail(self):
        print(f"Employee designation is : {self.Designation}")

class Developer(Employee):
        def __init__(self, Employe_name, Employe_Id, Designation):
            super().__init__(Employe_name,Employe_Id)
            self.Designation = Designation

        def d_detail(self):
            print(f"Employee designation is : {self.Designation}")


m = Manager("Ali Khan",123423,"Branch Manager")
m.e_detail()
m.m_detail()
d = Developer("Ali Muhammad",45676,"Senior Developer")
d.e_detail()
d.d_detail()