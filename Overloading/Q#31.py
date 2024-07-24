from multipledispatch import dispatch

class MathOperation:
    @dispatch(int , int)
    def addition(self, a , b ):
        print("Addition of two integer is",a+b)

    @dispatch(float, float)
    def addition(self, a , b ):
        print("Addition of two float number is".format(a + b))

    @dispatch(list)
    def addition(self, numbers):
        sum = 0
        for num in numbers:
            sum = sum + num
        print("Addition of list is ", sum)



m = MathOperation()
m.addition([1,2,3,4])
