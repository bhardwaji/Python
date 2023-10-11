from tkinter import *

root = Tk()
root.geometry("500x500")


def post():
    f = open("Data.txt", "w")
    if foodservicevalue.get() == 1:
        foodservice = "Yes"
    else:
        foodservice = "No"
    f.write(
        f"name = {namevalue.get()}\n  phone = {phonevalue.get()} \n gendervalue = {gendervalue.get()} \n emergency value = {emergencyvalue.get()} \n payment mode value = {paymentmodevalue.get()} \n food service = {foodservice}"
    )


Label(
    root,
    text="Welcome to shimla",
    font=("impact", 15, "bold"),
    fg="red",
    borderwidth=10,
    bg="black",
).grid(row=0, column=3)


name = Label(root, text="Name").grid(row=1, column=2)
phone = Label(root, text="phone").grid(row=2, column=2)
gender = Label(root, text="gender").grid(row=3, column=2)
emergency = Label(root, text="emergency").grid(row=4, column=2)
paymentmode = Label(root, text="paymentmode").grid(row=5, column=2)


namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue).grid(row=1, column=3)
phoneentry = Entry(root, textvariable=phonevalue).grid(row=2, column=3)
genderentry = Entry(root, textvariable=gendervalue).grid(row=3, column=3)
emergencyentry = Entry(root, textvariable=emergencyvalue).grid(row=4, column=3)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue).grid(row=5, column=3)


# checkbox
foodservice = Checkbutton(
    root,
    text="Want to book a meal",
    variable=foodservicevalue,
).grid(row=6, column=3)


# button
Button(text="Submit", command=post).grid(row=7, column=3)


root.mainloop()
