import os
print("****Program To Read Data From Files********")
print(f'''
Do you want to read Files
1.Yes
2.No
''')
while True:
    uc = input("Enter Your Choice : ")
    if uc=="1":
        print("1")
        break
    elif uc =="2":
        print("Gud Bye Sir/Mam")
        exit()

    else:
        print("wrong input")
print(" *****Files*****")
print()
num = 0
filelist = os.listdir()
for i in filelist :
    print(num ,":",end="")
    print(i)
    num = num+ 1
print("Select The file ")
uc= int(input("please enter the choice "))
filename =filelist[uc]

f = open(filelist[uc],"r")
print(f.read())
f.close()