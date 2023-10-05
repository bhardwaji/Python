import os
print("**data entry program**")

def data():
    name = input("Please Enter Name of file")
    extension = ".txt"
    global filename
    filename = name + extension
    return filename

def insertData(filename):
    if os.path.isfile(f"{filename}") == True :
        print("File already present")
    else:
        f = open(filename,"w")
        print("file created")
        print("Please Enter Data")

        name= input("enter name :")
        age = input("enter age")
        f.write(f"The name is entered is {name} \nage is {age}")
        f.close()
        f =open(filename)
        print("data entered is :", end=" ")
        print(f.read())


        exit()


while True :
    try:
      user_input = int(input('''
        do you want to add data into files
        1. yes
        2. No
              '''))

      if user_input==1 :
         data()
         insertData(filename)
      elif user_input==2 :
            exit()
      else:
          print(f"{user_input} : is not a correct input . please try again")
    except Exception as e:
        print(f" (datatype error) wrong input please try again")


