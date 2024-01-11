from snownlp import SnowNLP
import tkinter as tk
import matplotlib.pyplot as plt
import marshal
from snownlp.utils.frequency import AddOneProb
import gzip
from snownlp import sentiment
from zhujiemian import happyall
import numpy as np
import pandas as pd
import csv
def graphwindow():
    fig = plt.figure()
    ad = pd.read_table('GDP_Satisfaction.csv', sep=',')
    X = ad.iloc[:, 1]
    Y = ad.iloc[:, 2]

    ax1 = fig.add_subplot(1, 1, 1)

    # 设置标题
    ax1.set_title('Record of Emotional Points')
    # 设置横坐标名称
    ax1.set_xlabel('Average Emotional Point')
    # 设置纵坐标名称
    ax1.set_ylabel('Variance of Emotional Point')

    ax1.scatter(X, Y, c='k', marker='.')
    plt.show()