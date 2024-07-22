n=int(input("Enter no of element you want to enter in list:  "))
l=[]
for i in range(n):
    a=int(input("Enter the element in list: "))
    l.append(a)
print("no of element is list",l)
order_list=l.sort()
print("smallest no is",l[0])
print("largest no is ",l[3])

