#!/usr/bin/env python
# coding=utf-8

import tkinter as tk

window = tk.Tk()
window.title('Entry')
window.geometry('200x200')


def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)



# 创建输入框 entry , 用户输入的内容都显示为 *
e = tk.Entry(window, show='*')
e.pack()

# 创建按钮分别触发两种情况
b1 = tk.Button(window, text='insert point', width=15, height=2,command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()

# 创建文本框用于显示
t = tk.Text(window, height=2)
t.pack()



window.mainloop()

