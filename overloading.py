class A:
    def sub(self):
        print("Welcome")
    def sub(self,name=''):
        print("Welcome",self.name)
    def sub(self,name='',surname=''):
        print("Welcome ",name,surname)

obj=A()
obj.sub()
obj.sub("ali")
obj.sub("asif","Javed")