#  *_* coding:utf8 *_*
import tkinter
from tkinter import *

fire = 7
progress = 1
cnt=0

#计算当前鬼火，ob是否推动鬼火条（0/1），ob2减加（0/1）
def fire_cal(ob,ob2,num):
    global fire
    global progress
    global cnt
    if ob2 == 0:
        fire -= num
        if fire < 0:
            fire = 0
    else:
        fire += num
        if fire > 8:
            fire = 8
    if ob==0:
        progress+=1
        if progress>5:
            fire+=3+cnt
            if fire > 8:
                fire = 8
            cnt+=1
            if cnt>2:
                cnt=2
            progress=1




#减火函数，ob=0推动鬼火条，ob=1额外扣火
def fire_sub(ob,num):
    fire_cal(ob, 0, num)
    lbl21.configure(text=fire)
    lbl22.configure(text=progress)

#加火函数，ob=0推动鬼火条，ob=1额外加火
def fire_add(ob,num):
    fire_cal(ob, 1, num)
    lbl21.configure(text=fire)
    lbl22.configure(text=progress)

def new():
    global fire
    fire=7
    global progress
    progress=1
    lbl21.configure(text=fire)
    lbl22.configure(text=progress)

if __name__ == '__main__':

    window = Tk()
    window.title("鬼火计算器 v1.0")
    window.geometry("410x690")
    #标签

    lbl = Label(window, text="对方当前鬼火数：",font=("Arial Bold", 20))
    lbl.grid(row=0,column=0,columnspan=3)

    lbl21 = Label(window, text=fire,font=("Arial Bold", 20))
    lbl21.grid(row=0, column=3)

    lbl2 = Label(window, text="当前鬼火行动条：",font=("Arial Bold", 20))
    lbl2.grid(row=1,column=0,columnspan=3)

    lbl22 = Label(window, text=progress, font=("Arial Bold", 20))
    lbl22.grid(row=1, column=3)

    lbl3 = Label(window, text='-'*100, font=("Arial Bold", 10))
    lbl3.grid(row=2, column=0, columnspan=5)

    lbl4 = Label(window, text='行动时鬼火变化（会推动鬼火条）', font=("Arial Bold", 12))
    lbl4.grid(row=3, column=0, columnspan=5)

    lbl5 = Label(window, text='减', font=("Arial Bold", 14))
    lbl5.grid(row=4, column=0, columnspan=5)

    btn = Button(window, text="0火",command=lambda: fire_sub(0,0),font=("Arial Bold", 20))
    btn.grid(row=6,column=0)
    btn2 = Button(window, text="1火",command=lambda: fire_sub(0,1), font=("Arial Bold", 20))
    btn2.grid(column=1, row=6)
    btn3 = Button(window, text="2火",command=lambda: fire_sub(0,2), font=("Arial Bold", 20))
    btn3.grid(column=2, row=6)
    btn4 = Button(window, text="3火", command=lambda: fire_sub(0,3),font=("Arial Bold", 20))
    btn4.grid(column=3, row=6)
    btn5 = Button(window, text="4火", command=lambda: fire_sub(0,4),font=("Arial Bold", 20))
    btn5.grid(column=4, row=6)
    btn6 = Button(window, text="5火", command=lambda: fire_sub(0,5),font=("Arial Bold", 20))
    btn6.grid(column=0, row=7)
    btn7 = Button(window, text="6火", command=lambda: fire_sub(0,6),font=("Arial Bold", 20))
    btn7.grid(column=1, row=7)
    btn8 = Button(window, text="7火", command=lambda: fire_sub(0,7),font=("Arial Bold", 20))
    btn8.grid(column=2, row=7)
    btn9 = Button(window, text="剩余全部", command=lambda: fire_sub(0,8),font=("Arial Bold", 20))
    btn9.grid(column=3, row=7,columnspan=2)

    lbl6 = Label(window, text='加', font=("Arial Bold", 14))
    lbl6.grid(row=8, column=0, columnspan=5)

    btn21 = Button(window, text="1火", command=lambda: fire_add(0,1), font=("Arial Bold", 20))
    btn21.grid(column=0, row=9,columnspan=2)
    btn22 = Button(window, text="2火", command=lambda: fire_add(0,2), font=("Arial Bold", 20))
    btn22.grid(column=2, row=9)
    btn23 = Button(window, text="3火", command=lambda: fire_add(0,3), font=("Arial Bold", 20))
    btn23.grid(column=3, row=9,columnspan=2)

    lbl7 = Label(window, text='-' * 100, font=("Arial Bold", 10))
    lbl7.grid(row=10, column=0, columnspan=5)

    lbl8 = Label(window, text='额外鬼火变化（不会推动鬼火条）', font=("Arial Bold", 12))
    lbl8.grid(row=11, column=0, columnspan=5)

    lbl9 = Label(window, text='加', font=("Arial Bold", 14))
    lbl9.grid(row=12, column=0)

    btn31 = Button(window, text="1火", command=lambda: fire_add(1,1), font=("Arial Bold", 20))
    btn31.grid(column=1, row=12)
    btn32 = Button(window, text="2火", command=lambda: fire_add(1,2), font=("Arial Bold", 20))
    btn32.grid(column=2, row=12)
    btn33 = Button(window, text="3火", command=lambda: fire_add(1, 3), font=("Arial Bold", 20))
    btn33.grid(column=3, row=12)
    btn33 = Button(window, text="4火", command=lambda: fire_add(1, 4), font=("Arial Bold", 20))
    btn33.grid(column=4, row=12)

    lbl10 = Label(window, text='减', font=("Arial Bold", 14))
    lbl10.grid(row=13, column=0)

    btn41 = Button(window, text="1火", command=lambda: fire_sub(1, 1), font=("Arial Bold", 20))
    btn41.grid(column=1, row=13)
    btn42 = Button(window, text="2火", command=lambda: fire_sub(1, 2), font=("Arial Bold", 20))
    btn42.grid(column=2, row=13)
    btn43 = Button(window, text="3火", command=lambda: fire_sub(1, 3), font=("Arial Bold", 20))
    btn43.grid(column=3, row=13)
    btn43 = Button(window, text="4火", command=lambda: fire_sub(1, 4), font=("Arial Bold", 20))
    btn43.grid(column=4, row=13)

    lbl11 = Label(window, text='-' * 100, font=("Arial Bold", 10))
    lbl11.grid(row=14, column=0, columnspan=5)

    btn51 = Button(window, text="新的开局", command=new, font=("Arial Bold", 30))
    btn51.grid(column=0, row=15,columnspan=5)
    lbl12 = Label(window, text='默认有火灵', font=("Arial Bold", 10))
    lbl12.grid(row=16, columnspan=5, pady=10)

    lbl12 = Label(window, text='Developed by 吴树山 ', font=("Arial Bold", 8))
    lbl12.grid(row=17, sticky=E,columnspan=5,pady=10)


    window.mainloop()