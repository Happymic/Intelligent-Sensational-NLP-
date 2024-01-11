from snownlp import SnowNLP
import tkinter as tk
import matplotlib.pyplot as plt
import marshal
from snownlp.utils.frequency import AddOneProb
import gzip
from snownlp import sentiment
import datetime as dt
from zhujiemian import happyall
import numpy as np
from cundang import graphwindow

def zhixiebiao():
    zhixie = tk.Tk()
    zhixie.title('致谢名单')
    zhixie.geometry('500x300')
    zhixie.configure(background="#138EC7")

    zhixiewindow = tk.Listbox(zhixie, width=53, height=10, bg="white", fg="black")

    zhixiewindow.place(x=10, y=10)
    zhixiewindow.insert('anchor',"首先感谢沫凡老师给我们传授高端的AI技术","其次感谢HowMany哥，小洁和椿雨老师在整个营地指导我们","视频来源：油管","https://www.youtube.com/watch?v=45X0Q1d6Jwk","https://www.youtube.com/watch?v=sF5HeqPBTjY","编程语言：Python","视频背景音乐：The New Day-Mark Petrie以及Last Reunion-Peter Roe","最后十分感谢腾讯爸爸给了我们这次宝贵的夏令营机会！")