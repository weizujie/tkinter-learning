#!/usr/bin/env python
# coding=utf-8

import tkinter as tk

window = tk.Tk()
window.title('Label')
window.geometry('300x200')

l = tk.Label(
    window,
    text = 'OMG!This is TK!', # 标签的文字
    bg = 'green', # 背景颜色
    font = ('Arial', 12), # 字体和字体大小
    width = 15, height = 2, # 标签的长和宽
)

l.pack() # 固定窗口位置

window.mainloop()


