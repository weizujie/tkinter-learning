#!/usr/bin/env python
# coding=utf-8

import tkinter as tk

window = tk.Tk()
window.title('Radiobutton')
window.geometry('300x200')


var = tk.StringVar()
l = tk.Label(
    window, 
    bg='yellow',
    width = 20,
    text = 'empty'
)
l.pack()


def print_selection():
    l.config(text='you have selected ' + var.get())


list_ = ['A', 'B', 'C', 'D']
for i in list_:
    r1 = tk.Radiobutton(
        window,
        bg = 'yellow',
        text = 'Option {}'.format(i),
        variable = var, value= i, # 当鼠标选中其中一个选项，把value的值A放到变量var中，然后赋值给variable
        command = print_selection,
    )
    r1.pack()





window.mainloop()
