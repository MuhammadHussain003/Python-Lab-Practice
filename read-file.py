file_name=input("Enter a file name:   ")
try:
    a=open("file_name",'r')
    content=file_name.r()
    print("read the file")

except:
    print("File does not exist....")