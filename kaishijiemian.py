from tkinter import NE

from snownlp import SnowNLP
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import marshal
from snownlp.utils.frequency import AddOneProb
import gzip
from snownlp import sentiment
import datetime as dt
from zhujiemian import happyall
import numpy as np
from cundang import graphwindow
from beijingyemian import beijingchuangkou
from zhixiemingdan import zhixiebiao
startup = tk.Tk()
startup.title('开始界面')
startup.geometry('500x700')

#创建一个图片管理类
photo = tk.PhotoImage(file="tencentlogo.gif")#file：t图片路径
imgLabel = tk.Label(startup,image=photo)#把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)#自动对齐
'''
filename = tk.PhotoImage(file ="tencentlogo.gif")
image = canvas.create_image(100, 100, anchor=NE, image=filename)


qqlogo = tk.Canvas(startup, height=200, width=200)
image_file = tk.PhotoImage(file = "tencentlogo.gif")
image = canvas.create_image(0,0, image=image_file)
qqlogo.place(x=0,y=0)
'''
kaishib = tk.Button(startup, text='开始检测', width=10, height=2, bg="black", fg="green", command=happyall)
kaishib.place(x=40, y=630)
kaile = tk.Button(startup, text='查看记录', width=10, height=2, bg="black", fg="green", command=graphwindow)
kaile.place(x=260, y=630)

gushi = tk.Button(startup, text='项目背景', width=10, height=2, bg="black", fg="green", command=beijingchuangkou)
gushi.place(x=150, y=630)

zhixie = tk.Button(startup, text='致谢目录', width=10, height=2, bg="black", fg="green", command=zhixiebiao)
zhixie.place(x=370, y=630)
startup.mainloop()