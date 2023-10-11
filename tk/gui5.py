from tkinter import *


def login():
    print("the value of username is : ", uservalue.get())
    print("the value of password is :", passvalue.get())
    if uservalue.get() == "User" or passvalue.get() == "123":
        print("Login Sucessful")
    else:
        print("login failed")


root = Tk()
root.geometry("500x500")
user = Label(root, text="Username")
user.grid(row=0, column=0)  # row and #Column in grid

passw = Label(root, text="Password")
passw.grid(row=1, column=0)
# vaerbale classes in tkinter  1. booleanvar, Doublevar ,intvar ,string var


uservalue = StringVar()
passvalue = StringVar()

Userentry = Entry(root, textvariable=uservalue)
Passentry = Entry(root, textvariable=passvalue)
Userentry.grid(row=0, column=1)
Passentry.grid(row=1, column=1)


# login
Button(text="Login", command=login).grid()

root.mainloop()
