from snownlp import SnowNLP

import tkinter as tk
import marshal
from snownlp.utils.frequency import AddOneProb

import gzip
from snownlp import sentiment


def happyall():
    global times, intro
    window = tk.Toplevel()
    window.title('指数测试')
    window.geometry('500x600')
    # window.configure(background="white")
    intro = tk.Listbox(window, width=30, height=2, bg="#6BE61A", fg="black")
    intro.place(x=120, y=670-200)
    intro.insert("anchor", "首先请在下面输入你的名字。")
    intro.insert("anchor", "First, please entry your name below.")
    e = tk.Entry(window, width=46, bd=5)
    e.place(x=5, y=760-200)
    times = 0
    image_file = tk.PhotoImage(file="head.png")

    def analyse(sentence_list):
        res = 0
        for s in sentence_list:
            # cal s sentiments
            pass
        res /= len(sentence_list)
        return res
    

    def load_extra_dict(fname, iszip=True):
        sent = sentiment.classifier.classifier
        if not iszip:
            data = marshal.load(open(fname, 'rb'))
        else:
            try:
                data = marshal.loads(gzip.open(fname, 'rb').read())
            except IOError:
                data = marshal.loads(open(fname, 'rb').read())
        for d in data["d"].items():
            if d[0] not in sent.d:
                sent.d[d[0]] = AddOneProb()
            for word, num in d[1]["d"].items():
                sent.d[d[0]].add(word, num)
        sent.total = sum(map(lambda x: sent.d[x].getsum(), sent.d.keys()))


    load_extra_dict("./test_sentiment.marshal.3")
    '''
    也可以分两到三种
    一种平均，一种每个问题都加百分比，对比，然后讲
    '''


    def fasong():
        global intro
        global times
        global send1
        global send2
        global send3
        global send4
        global send5
        global send6
        times = times + 1
        print(times)
        X = 40
        intro.destroy()
        ai_width = 50
        def create_img(y):
            c = tk.Canvas(window, width=30, height=30)
            c.place(x=3, y=y)
            c.create_image(0, 0, anchor="nw", image=image_file)
        if times == 1:
            send1 = e.get()  # 这个是第一次返回的输入
            lb1 = tk.Listbox(window, width=30, height=1, bg="#6BE61A", fg="black")
            lb1.place(x=200, y=10)
            lb1.insert("anchor", send1)
            r = send1
            with open('input_chains.txt', 'w') as f:  # 打开 input_chains.txt
                f.write(r + '\n')
            qb1 = tk.Listbox(window, width=ai_width, height=2, bg="white", fg="black")
            # qb1.insert("end", send1, "你好，请问您的近日的睡眠怎么样？")
            qb1.insert("end", send1, "你好，请问您的睡眠怎么样？Hi, how good was your sleep?")
            qb1.place(x=X, y=70-30)
            e.delete(0, 'end')

            create_img(70-30)

        if times == 2:
            send2 = e.get()  # 这个是第二次返回的输入
            lb2 = tk.Listbox(window, width=30, height=2, bg="#6BE61A", fg="black")
            lb2.place(x=200, y=113-30)
            lb2.insert("anchor", send2)
            r = send2
            with open('input_chains.txt', 'a') as f:  # 打开 input_chains.txt
                f.write(r + '\n')
            qb2 = tk.Listbox(window, width=ai_width, height=1, bg="white", fg="black")
            # qb2.insert("anchor", "下一题，请问你最近有没有感到什么压力")
            qb2.insert("anchor", "请问你有没有感到压力?\nDo you feel depressed lately?")
            qb2.place(x=X, y=173-50)
            e.delete(0, 'end')
            create_img(173-50)
        if times == 3:
            send3 = e.get()  # 这个是第三次返回的输入
            lb3 = tk.Listbox(window, width=30, height=2, bg="#6BE61A", fg="black")
            lb3.place(x=200, y=150)
            lb3.insert("anchor", send3)
            r = send3
            with open('input_chains.txt', 'a') as f:  # 打开 input_chains.txt
                f.write(r + '\n')
            qb3 = tk.Listbox(window, width=ai_width, height=1, bg="white", fg="black")
            # qb3.insert("anchor", "下一题，请问当遇到使自己失望的事时，你的反应如何？")
            qb3.insert("anchor", "当挫败时你反应如何？\nWhat would you do when depressed?")
            qb3.place(x=X, y=190)
            e.delete(0, 'end')
            create_img(190)
        if times == 4:
            send4 = e.get()  # 这个是第四次返回的输入
            lb4 = tk.Listbox(window, width=30, height=2, bg="#6BE61A", fg="black")
            lb4.place(x=200, y=190+25)
            lb4.insert("end", send4)
            r = send4
            with open('input_chains.txt', 'a') as f:  # 打开 input_chains.txt
                f.write(r + '\n')
            qb4 = tk.Listbox(window, width=ai_width, height=1, bg="white", fg="black")
            # qb4.insert("anchor", "下一题，在与周围人相处时，你的自我感觉如何？")
            qb4.insert("anchor", "与人相处时你感觉如何？\nHow do you feel when staying in a group?")
            qb4.place(x=X, y=190+25+45)
            e.delete(0, 'end')
            create_img(190+25+45)
        if times == 5:
            send5 = e.get()  # 这个是第五次返回的输入
            lb5 = tk.Listbox(window, width=30, height=2, bg="#6BE61A", fg="black")
            lb5.place(x=200, y=190+25*2+45)
            lb5.insert("end", send5)
            r = send5
            with open('input_chains.txt', 'a') as f:  # 打开 input_chains.txt
                f.write(r + '\n')
            qb5 = tk.Listbox(window, width=ai_width, height=1, bg="white", fg="black")
            # qb5.insert("anchor", "最后，请问你在遭遇不良情绪时怎么处理？")
            qb5.insert("anchor", "你怎么处理差情绪？\nwhat would you do when you feel bad?")
            qb5.place(x=X, y=190+25*2+45*2)
            e.delete(0, 'end')
            create_img(190+25*2+45*2)
        if times == 6:
            send6 = e.get()  # 这个是返回的输入
            lb6 = tk.Listbox(window, width=30, height=2, bg="#6BE61A", fg="black")
            lb6.place(x=200, y=190+25*3+45*2, )
            lb6.insert("end", send6)
            qb6 = tk.Listbox(window, width=24, height=1)
            qb6.insert("anchor", "输入任意文字加载您的报告")
            qb6.place(x=X, y=190+25*3+45*3, )
            r = send6

            with open('input_chains.txt', 'a') as f:  # 打开 input_chains.txt
                f.write(r + '\n')
            e.delete(0, 'end')
            create_img(190+25*3+45*3)
        if times == 7:
            send7 = e.get()
            qb7 = tk.Listbox(window, width=ai_width, height=1)
            # qb7.insert("anchor", "好的:) 正在加载您的报告。。。")
            qb7.insert("anchor", "好的:) 正在加载您的报告。\nProcessing...")
            qb7.place(x=X, y=190+25*4+45*3)
            with open('input_chains.txt', 'r') as f:  # 打开 input_chains.txt
                data = f.readlines()
            res = analyse(data)
            create_img(190+25*4+45*3)
            # 进⾏行行训练
            #      from utils import load_extra_dict  # 导⼊入模型

            name = send1
            first = send2
            second = send3
            third = send4
            fourth = send5
            fifth = send6
            sixth = send7

            a = SnowNLP(first).sentiments

            data_list = [[name], [SnowNLP(first).sentiments], [SnowNLP(second).sentiments], [SnowNLP(third).sentiments],
                         [SnowNLP(fourth).sentiments], [SnowNLP(fifth).sentiments], [SnowNLP(sixth).sentiments]],

            print(data_list)

            sum = SnowNLP(first).sentiments + SnowNLP(second).sentiments + SnowNLP(third).sentiments + SnowNLP(
                fourth).sentiments + SnowNLP(fifth).sentiments
            average = sum / 5

            variance= 10/5*(((SnowNLP(first).sentiments)-average)**2+((SnowNLP(second).sentiments)-average)**2+(
                    (SnowNLP(third).sentiments)-average)**2+((SnowNLP(fourth).sentiments)-average)**2+(
                    (SnowNLP(fifth).sentiments)-average)**2)
            print(average)
            print(variance)

            reportwindow = tk.Tk()
            reportwindow.title('预测报告')
            reportwindow.geometry('350x600')
            reportwindow.configure(background="grey")
            intro = tk.Listbox(reportwindow, width=36, height=8)
            intro.place(x=10, y=10)
            feedbackbox = tk.Listbox(reportwindow, width=36, height=8)
            feedbackbox.place(x=10, y=200)
            chartfeedback = tk.Listbox(reportwindow, width=36, height=8)
            chartfeedback.place(x=10, y=400)

            with open('input_chains.txt', 'r') as f:  # 打开 input_chains.txt
                r = f.read()
            intro.insert("end", str(name), str("您好，您的回答分别是. Here are your answers："))
            intro.insert("end", str(first))
            intro.insert("end", str(second))
            intro.insert("end", str(third))
            intro.insert("end", str(fourth))
            intro.insert("end", str(fifth))
            intro.insert("end", str("数据AI平均值为, Average score：" + str(average)))

            if average >= 0.6:
                feedbackbox.insert("end", str("从整体上来讲，您的心理状况为良好，"))
                feedbackbox.insert("end", str("You looks great."))
                feedbackbox.insert("end", str("祝您一切顺利！"))
                feedbackbox.insert("end", str("Good luck and stay safe."))
            elif average < 0.6 and average >= 0.4:
                feedbackbox.insert("end", (str("从整体上来讲，您的心理状况有小部分抑郁，")))
                feedbackbox.insert("end", (str("Generally, you're little depressed,")))
                feedbackbox.insert("end", (str("平常请多与家人和朋友沟通，")))
                feedbackbox.insert("end", (str("talk more with your friends would help you,")))
                feedbackbox.insert("end", (str("注意培良好的饮食、作息及工作等习惯。")))
                feedbackbox.insert("end", (str("and keep a healthy dietary/living habit will help.")))
            elif average < 0.4:
                feedbackbox.insert("end", (str("您的心理状况极为堪忧，")))
                feedbackbox.insert("end", (str("You're experiencing a mental problem,")))
                feedbackbox.insert("end", (str("请尽快向心理医生咨询。")))
                feedbackbox.insert("end", (str("please talk to a psychologist ASAP.")))
                feedbackbox.insert("end", (str("千万不要想不开喔")))
            with open('finalinput_chains.csv', 'a') as f:
                f.write('\n'+name+','+str(average)+','+str(variance))
                print(average)
                f.close()

    b = tk.Button(window, text='发送', width=6, height=2, bg="green", fg="green", command=fasong)
    b.place(x=440, y=760-200)

    window.mainloop()
