from tkinter import *

root = Tk()
root.geometry("1000x500")


def hello():
    print("hello Tkinter Buttons")


def name():
    print("name is shubham")


frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="ne")


b1 = Button(frame, fg="red", text="Print-Now", command=hello)
b1.pack(side=LEFT, padx=15)
b2 = Button(frame, fg="red", text="tell-me-name-Now", command=name)
b2.pack(side=LEFT, padx=15)
b3 = Button(frame, fg="red", text="phone no")
b3.pack(side=LEFT, padx=15)
b4 = Button(frame, fg="red", text="help")
b4.pack(side=LEFT, padx=15)


root.mainloop()
