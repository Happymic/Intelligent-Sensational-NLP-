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
# -*- coding:utf-8 -*-


def beijingchuangkou():
    beijing = tk.Tk()
    beijing.title('项目背景')
    beijing.geometry('500x500')
    beijing.configure(background="#138EC7")

    story1 = tk.Listbox(beijing, width=53, height=10, bg="white", fg="black")


    story1.place(x=10, y=10)
    story1.insert('anchor',"老子曾说过：上善若水，水善利万物而不争。这是我们对科技向善的理解。", "科技改变人的生活，但发达的科技应该建立在人类道德观念之上。", "在当今的21世纪，面对社会带来的压力，人们的心理状况变得越来越不可忽视，", "大部分的人都会面临一定的心理问题。由于做心理测评需要进行全方位的评估，", "测评面广、耗时长，而社会上也缺乏高水平的专业心理测评师，", "许多人经常没有办法知道自己的心理是否健康，", "因此也没有办法进行及时干预或治疗。")

    story2 = tk.Listbox(beijing, width=53, height=10, bg="white", fg="black")
    story2.place(x=10, y=230)
    story2.insert('anchor',"个人的心理健康状况会影响个人的生活、工作、交友及家庭相处等各各方面。", "在大大小小的公司招聘时，招聘者必须清楚地了解求职者的心理状况，", "以此作为招聘的一个重要指标来更精准地区分求职者们的能力和心理健康。", "然而应聘者的数量如此庞大，应聘者的情况差异也很大，", "必然会给公司的人力资源部或心理测评师带来繁重工作量。", "那么如何才能制定快速而精准的方法去衡量求职者的心理状况呢？","这就是我们设计这个程序的原因!")