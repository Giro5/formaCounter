from tkinter import *
from tkinter import messagebox
 
root = Tk()
root.title("Counter")
root.geometry("200x200")

coun = 0
coun_label_text = StringVar()
coun_label_text.set(str(coun))
coun_label = Label(textvariable=coun_label_text)
coun_label.grid(row=1, column=0, padx=20, pady=20)

def plus1():
    global coun
    coun+=1
    coun_label_text.set(str(coun))

def minus1():
    global coun
    coun-=1
    coun_label_text.set(str(coun))

def Clear():
    global coun
    coun=0
    coun_label_text.set(str(coun))

plus_button = Button(text="+", command=plus1)
plus_button.grid(row=0, column=0, padx=20, pady=10)

minus_button = Button(text="-", command=minus1)
minus_button.grid(row=2, column=0, padx=20, pady=10)

clear_button = Button(text="Сброс", command=Clear)
clear_button.grid(row=1, column=3, padx=40, pady=20)

root.mainloop()


