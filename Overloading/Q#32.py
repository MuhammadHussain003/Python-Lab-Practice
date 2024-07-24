from multipledispatch import dispatch
class StringManipulator:

     @dispatch(str,str)
     def concatenation(self,a,b):
         print("Concatenation of two string is : ",a+b)

     @dispatch(list)
     def concatenation(self, a):
         print(f"Concatenation of two string is : {''.join(a)}")

s = StringManipulator()
s.concatenation("How are you","i am pine")
s.concatenation(["hello","world"])
