class Shoppingcart:
    __list1=[]
    def __init__(self,list1):
        self.__list1=list1

    def add(self,):
        print("items in list is",self.__list1)

    def remove(self,r):
        for index in range(0,len(self.__list1)):
            flag=None
            if(self.__list1[index]==r):
                flag=self.__list1[index]
                self.__list1.pop(index)
                break
            else:
                flag=False
        if(flag):
            print(f"The {flag} removed successfully...")

        else:
            print(" Not found in the list")

    def search_item(self,i):
        for index  in range(0,len(self.__list1)):
            flag=None
            if (self.__list1[index] == i):
                flag = self.__list1[index]
                break
            else:
                flag=False
        if(flag):
            print(f"The item {flag} are available in the list")
        else:
            print(f"items are not available in the list")







s=Shoppingcart(["apple","banana","mango"])
s.add()
s.remove("mango")
s.search_item("mango")



