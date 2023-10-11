from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x300")
# root.minsize(500, 300)
# root.maxsize(800, 500)


# # Back = PhotoImage(file="back.png")
# image = Image.open("back.jpg")
# photo = ImageTk.PhotoImage(image)
#
#
# background = Label(image=photo)
# background.pack()

title_label = Label(
    text="""
   Hi this is a text
and this is my gui 

""",
    background="red",
    fg="white",
    padx="12",
    pady="50",
    # font="impact 15 bold",
    font=("impact", 16, "bold"),
    borderwidth=3,
    relief=SUNKEN,
)
# important pack options
# anchor = "nw" ,"se"
# side = top bottom left right
# title_label.pack(anchor="se", side=TOP)
# title_label.pack(side="top")
# title_label.pack(side=BOTTOM, fill=X, anchor=SW)
title_label.pack(side=LEFT, fill=Y, anchor=SW)
# title_label.pack(side=BOTTOM, fill=X, anchor=SW, padx=30, pady=60)
# # side=BOTTOM, fill=X, anchor=SW, padx=30, pady=60
# title_label.pack(fill=Y)
root.mainloop()
