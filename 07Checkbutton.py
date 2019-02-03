#!/usr/bin/env python
# coding=utf-8

import tkinter as tk

window = tk.Tk()
window.title('CheckButton')
window.geometry('400x300')


l = tk.Label(
    window,
    text = 'empty',
    width = 15,
    bg = 'yellow'
)
l.pack()


def print_selection():
    if ((var1.get()==1) & (var2.get()==0)):
        l.config(text='I love only python.')

    elif ((var1.get()==0) & (var2.get()==1)):
        l.config(text='I love only c.')
    elif ((var1.get()==1) & (var2.get()==1)):
        l.config(text='I love both.')
    else:
        l.config(text='I do not love either.')



var1 = tk.IntVar()
c1 = tk.Checkbutton(
    window, 
    text = 'python',
    variable = var1,
    onvalue = 1, # 当选中这个 Checkbutton 时，onvalue 的值放到 var1 中，然后将 var1 的值赋值给 variable
    offvalue = 0,
    command = print_selection,
)
c1.pack()

var2 = tk.IntVar()
c1 = tk.Checkbutton(
    window, 
    text = 'c',
    variable = var2,
    onvalue = 1, # 当选中这个 Checkbutton 时，onvalue 的值放到 var1 中，然后将 var1 的值赋值给 variable
    offvalue = 0,
    command = print_selection,
)
c1.pack()









window.mainloop()
