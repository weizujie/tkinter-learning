#!/usr/bin/env python
# coding=utf-8

import tkinter as tk

window = tk.Tk()
window.title('Listbox')
window.geometry('200x200')

# 创建一个标签
var1 = tk.StringVar()
l = tk.Label(
    window,
    textvariable = var1,
    bg = 'yellow',
    width = 15,
    height = 2
)
l.pack()


def print_select():
    value = lb.get(lb.curselection()) # 获取当前选中的文本
    var1.set(value)


b1 = tk.Button(
    window,
    text = 'print selection',
    width = 15,
    height = 2,
    command = print_select,
)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44)) # 为变量设置值

# 创建Listbox
lb = tk.Listbox(
    window,
    listvariable=var2, # 将 var2 的值赋给 Listbox

)

# 创建一个 list 并将值讯号添加到 Listbox
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.pack()




window.mainloop()
