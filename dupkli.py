list1=[1,2,3,4,5,3,2,4,5,6,7,8,9,4,3]
duplicate_list=[]
for i in list1:
    if i not in duplicate_list:
        duplicate_list.append(i)

print("The list without duplicate element is ",duplicate_list)
