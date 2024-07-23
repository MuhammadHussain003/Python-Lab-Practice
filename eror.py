class MathOperations:

     def add(self,x, y):
         if isinstance(x, int) and isinstance(y, int):
          print("Addition of integers:",x+y)
     def add( self,x , y):
          if isinstance(x, float) and isinstance(y, float):
             print("Addition of float is ",x+y)



m = MathOperations()
m.add(2,2)