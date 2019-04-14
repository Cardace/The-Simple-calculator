from tkinter import *
import tkinter
import tkinter.font as tkFont
class Calc:
        def __init__(self):
            self.tk = tkinter.Tk()
            self.tk.title("垃圾计算器")
            #计算器不可改变设置
            self.tk.resizable(0,0)
            #显示的字体相关设置
            self.tk.showfont = tkFont.Font(self.tk,size=26)
            #程序界面字体设置
            self.tk.sysfont = tkFont.Font(self.tk,size=16)
            #显示输入和结果内容的文本框
            self.showEntry = tkinter.Entry(self.tk,width=20,justfy=tkinter.RIGHT,font=self.showfont,background="#ffffff")
            self.showEntry.grid(row=0,column=0,columnspan=4,pady=10)
            #7
            self.btn7 = tkinter.Button(self.tk,text="7",font=self.sysfont,command=lambda:self.insert("7"))
            self.btn7.grid(row=1,column=0,sticky=tkinter.N+tkinter.S+tkinter.W+tkinter.E)
            #8
            self.btn8= tkinter.Button(self.tk, text="8", font=self.sysfont,command=lambda:self.insert("8"))
            self.btn8.grid(row=1, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #9
            self.btn9 = tkinter.Button(self.tk, text="9", font=self.sysfont,command=lambda:self.insert("9"))
            self.btn9.grid(row=1, column=2, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #÷
            self.btn_div = tkinter.Button(self.tk, text="÷", font=self.sysfont,command=lambda:self.insert("÷"))
            self.btn_div.grid(row=1, column=3, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #4
            self.btn4 = tkinter.Button(self.tk, text="4", font=self.sysfont,command=lambda:self.insert("4"))
            self.btn4.grid(row=2, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #5
            self.btn5 = tkinter.Button(self.tk, text="5", font=self.sysfont,command=lambda:self.insert("5"))
            self.btn5.grid(row=2, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #6
            self.btn6 = tkinter.Button(self.tk, text="6", font=self.sysfont,command=lambda:self.insert("6"))
            self.btn6.grid(row=2, column=2, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #×
            self.btn_mul = tkinter.Button(self.tk, text="×", font=self.sysfont,command=lambda:self.insert("×"))
            self.btn_mul.grid(row=2, column=3, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #1
            self.btn1 = tkinter.Button(self.tk, text="1", font=self.sysfont,command=lambda:self.insert("1"))
            self.btn1.grid(row=3, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #2
            self.btn2 = tkinter.Button(self.tk, text="2", font=self.sysfont,command=lambda:self.insert("2"))
            self.btn2.grid(row=3, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #3
            self.btn3 = tkinter.Button(self.tk, text="3", font=self.sysfont,command=lambda:self.insert("3"))
            self.btn3.grid(row=3, column=2, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #-
            self.btn_sub = tkinter.Button(self.tk, text="-", font=self.sysfont,command=lambda:self.insert("-"))
            self.btn_sub.grid(row=3, column=3, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #0
            self.btn0 = tkinter.Button(self.tk, text="0", font=self.sysfont,command=lambda:self.insert("0"))
            self.btn0.grid(row=4, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #.
            self.btn_point = tkinter.Button(self.tk, text=".", font=self.sysfont,command=lambda:self.insert("."))
            self.btn_point.grid(row=4, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #=
            self.btn_equ = tkinter.Button(self.tk, text="=", font=self.sysfont,command=self.calc)
            self.btn_equ.grid(row=4, column=2, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
            #+
            self.btn_add = tkinter.Button(self.tk, text="+", font=self.sysfont,command=lambda:self.insert("+"))
            self.btn_add.grid(row=4, column=3, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

            self.tk.mainloop()
        def insert(self,stringtemp):
            self.showEntry.insert(tkinter.END,stringtemp)
        def calc(self):
            exp=self.showEntry.get().strip()
            exp=exp.replace("×","*")
            exp=exp.replace("÷","/")
            result=eval(exp)
            self.showEntry.delete(0,tkinter.END)
            self.showEntry.insert(tkinter.END,result)



