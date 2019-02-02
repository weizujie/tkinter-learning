#!/usr/bin/env python
# coding=utf-8

import tkinter as tk
window = tk.Tk()
window.title('Label')
window.geometry('300x200')


var = tk.StringVar() # 这时字体变量存储器

# 标签
l = tk.Label(
    window,
    textvariable = var, # 用 textvariable 代替 text, 因为这个可以变化
    bg = 'green', # 背景颜色
    font = ('Arial', 12), # 字体和字体大小
    width = 15, height = 2, # 标签的长和宽
)
l.pack() # 固定窗口位置


on_hit = False
def hit_me():
    global on_hit
    if on_hit == False: # 从 False 变成 True
        on_hit = True
        var.set('you hit me') # 设置标签的文字
    else: # 从 True 状态变成 False 
        on_hit = False
        var.set('') # 设置文子为空

# 按钮
b = tk.Button(
    window,
    text = 'hit me', # 按钮上的文字
    width = 15,
    height = 2,
    command = hit_me # 点击按钮执行命令
)
b.pack()

window.mainloop()



