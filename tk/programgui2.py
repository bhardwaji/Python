from tkinter import *


def login():
    if usernamevalue.get() == "admin" and passwordvalue.get() == "123":
        print("login")
    else:
        print("login failed")


root = Tk()
root.title("Login")
root.geometry("600x400")


username = Label(root, text="Username", font=["Impact ,15 , Bold"], relief=GROOVE).grid(
    row=0, column=0
)
password = Label(root, text="Password", font=["Impact ,15 , Bold"]).grid(
    row=1, column=0
)


usernamevalue = StringVar()
passwordvalue = StringVar()


text1 = Entry(root, textvariable=usernamevalue).grid(row=0, column=1)

text2 = Entry(root, textvariable=passwordvalue).grid(row=1, column=1)


b1 = Button(root, text="Login", command=login).grid(row=2, column=1)
root.mainloop()
