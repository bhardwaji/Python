
import random


print("Enter Details")
print('''
Details Required
Addhar no :
Full Name :
Fathers Name :
gender (male/female)
Address :
phone number :
emailid :
''')

def insertData():
    global aadhar_No, fullname, fathersName, gender, address, phoneno, email
    aadhar_No = input("Please Enter Your Aadhar Card Number")
    fullname=  input("Please Enter Your full name")
    fathersName = input("Please Enter Your Fathersname")
    while True:
        gender = input('''
        1. Male
        2. Female
        ''')
        try:
            if gender=="1":
                gender = "Male"
                break
            elif gender =="2":
                gender= "Female"
                break
            else :
                print("not a correct value")
        except Exception as e:
            print("gender wrong enter again")

    address = input("Please Enter Your address")
    phoneno=input("Please Enter Your phone  number")
    email = input("Please Enter Your email")

def checkdata():
    print(f'''
    Data Entered :
*****************************************************
Addhar no : {aadhar_No}
Full Name : {fullname}
Fathers Name : {fathersName}
gender (male/female) : {gender}
Address : {address}
phone number : {phoneno}
emailid : {email}
*****************************************************
    ''')
def confirmData():
    confirmdata = input('''please confirm data do you want add this data into file or reenter the data:
1. Yes Data Inserted
2. Reenter the Data
    ''')
    while True:
        try:
            if confirmdata == '1':
                datainsert()
                break
            elif confirmdata == '2':
                insertData()
                checkdata()
                confirmData()
                break
            else:
                print("please enter 1 or 2 to confirm")
                confirmData()
        except Exception as e:
            print("some problem is there")
            break
def file():

    name = random.randint(1,100)
    name = str(name)
    extension = ".txt"
    global filename
    filename = name+extension
    return filename

def datainsert():
    file()
    f =open(filename ,"w+")
    f.write(f'''*****************************************************
Addhar no : {aadhar_No}
Full Name : {fullname}
Fathers Name : {fathersName}
gender (male/female) : {gender}
Address : {address}
phone number : {phoneno}
emailid : {email}
*****************************************************''')

    print("**********Data inserted**********")


data = input("do you want to enter data y/n : ")
if data=="y":
    insertData()
    checkdata()
    confirmData()

else:
    exit()

