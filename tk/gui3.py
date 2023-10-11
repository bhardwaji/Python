# Home work
#
# # same directory  files need to print
# #newspaper


from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1000x500")
# frame
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l1 = Label(f1, text="Project Tkinter -PyCharm")
l1.pack(pady=142)
l1 = Label(f2, text="Welcome to Sublime text", fg="red")
l1.pack(pady=10)
root.mainloop()
