from multipledispatch import dispatch

class Calculator:
    @dispatch(int , int)
    def multiplication(self, a , b ):
        print("Multiplication of two integer is",a * b)

    @dispatch(float, float)
    def multiplication(self, a , b ):
        print("Multiplication of two float number is".format(a * b))

    @dispatch(list)
    def multiplication(self, numbers):
        sum = 1
        for num in numbers:
            sum = sum * num
        print("Multiplication of list is ", sum)



m = Calculator()
m.multiplication([1,2,3,4])
