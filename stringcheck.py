a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = input("Enter the operation you want to perform '+' , '-' , '*' , '/' : ")

if c=="+":
    print("The sum of ",a," and ",b," is :",a+b)
elif c=="-":
    print("The subtraction of ",a," and ",b," is :",a-b)
elif c=="*":
    print("The Multiplication of ",a," and ",b," is :",a*b)
elif c=="/":
    print("The division of ",a," and ",b," is :",a/b)
else:
    print("Invalid Operator")
