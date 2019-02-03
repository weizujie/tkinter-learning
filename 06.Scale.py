#!/usr/bin/env python
# coding=utf-8

import tkinter as tk

window = tk.Tk()
window.title('Scale')
window.geometry('400x300')

l = tk.Label(
    window,
    bg = 'yellow',
    width = 20,
    text = 'empty'
)
l.pack()


def print_selection(v):
    l.config(text='you have selected ' + v) # v 滚动条定位的数据    



s = tk.Scale(
    window, 
    label = 'Try me',
    from_= 5, to = 11, # 从5到11
    orient = tk.HORIZONTAL, # 滚动的方向HORIZONTAL是横向
    length = 200,  # 滚动条部件的长度, 像素单位
    showvalue = 0, # 
    tickinterval = 2,  # 坐标间隔
    resolution = 0.01, # 保留2位小数
    command = print_selection,
)
s.pack()




window.mainloop()
