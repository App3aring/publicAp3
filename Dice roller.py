import tkinter
from tkinter import *
import random

root = Tk()
root.geometry("400x400")

l1 = Label(root, font =("helvetica" ,260))


def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text = f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()

b1 = Button(root, text = "roll the dice!" ,foreground='blue' ,command=roll)
b1.place(x=300, y=0)
b1.pack()

root.mainloop()

