
# Shallow Copy
# list, object, tuble, dictonary
#
# class A:
#     item = "item"
#
# obj_a = A();
#
# obj_b = obj_a
#
# obj_b.key = 34345435345
#
#
# print(obj_a.key)
#
#
# #
#item



list_a =  [1, 2, 4]

list_b = list_a


print("list a", id(list_a))
print("list b", id(list_b))


#
#
# # Deep Copy
# # Int, float, bool, sting
#
#
# # number_a  = 40
# #
# # number_b  = number_a
# #
# # number_b = 30
# #
# #
# # print("Number a", number_a)
# # print("Number a", number_b )
