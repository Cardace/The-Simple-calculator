import tkinter

root = tkinter.Tk()
root.minsize(375,555)
root.title('calculator')


#界面布局
#显示面板
result = tkinter.StringVar()
result.set(0)                    #显示结果1，用于显示默认数字0
result2 = tkinter.StringVar()    #显示结果2，用于显示计算过程
result2.set('')

#显示板
label = tkinter.Label(root,font = ('楷体',20),bg = 'grey',bd ='9',fg = 'white',anchor = 'se',textvariable = result2)
label.place(width = 375,height = 170)
label2 = tkinter.Label(root,font = ('楷体',30),bg = 'grey',bd ='9',fg = 'white',anchor = 'se',textvariable = result)
label2.place(y = 170,width = 375,height = 60)


#数字键盘
btn7 = tkinter.Button(root,text = '7',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('7'))
btn7.place(x = 0,y = 285,width = 75,height = 55)
btn8 = tkinter.Button(root,text = '8',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('8'))
btn8.place(x = 75,y = 285,width = 75,height = 55)
btn9 = tkinter.Button(root,text = '9',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('9'))
btn9.place(x = 150,y = 285,width = 75,height = 55)

btn4 = tkinter.Button(root,text = '4',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('4'))
btn4.place(x = 0,y = 340,width = 75,height = 55)
btn5 = tkinter.Button(root,text = '5',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('5'))
btn5.place(x = 75,y = 340,width = 75,height = 55)
btn6 = tkinter.Button(root,text = '6',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('6'))
btn6.place(x = 150,y = 340,width = 75,height = 55)

btn1 = tkinter.Button(root,text = '1',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('1'))
btn1.place(x = 0,y = 395,width = 75,height = 55)
btn2 = tkinter.Button(root,text = '2',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('2'))
btn2.place(x = 75,y = 395,width = 75,height = 55)
btn3 = tkinter.Button(root,text = '3',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('3'))
btn3.place(x = 150,y = 395,width = 75,height = 55)
btn0 = tkinter.Button(root,text = '0',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressNum('0'))
btn0.place(x = 75,y = 450,width = 75,height = 55)

#运算符号按钮
btnac = tkinter.Button(root,text = 'C',bd = 0.5,font = ('楷体',20),fg = 'black',command = lambda :pressCompute('C'))
btnac.place(x = 0,y = 230,width = 75,height = 55)
btnback = tkinter.Button(root,text = '←',font = ('楷体',20),fg = 'black',bd = 0.5,command = lambda:pressCompute('b'))
btnback.place(x = 75,y = 230,width = 75,height = 55)
btndivi = tkinter.Button(root,text = '÷',font = ('楷体',20),fg = 'black',bd = 0.5,command = lambda:pressCompute('/'))
btndivi.place(x = 150,y = 230,width = 75,height = 55)
btncos = tkinter.Button(root,text = 'cos',font = ('楷体',20),fg = 'black',bd = 0.5,command = lambda:pressCompute('cos'))
btncos.place(x = 300,y = 395,width = 75,height = 55)
btnmul = tkinter.Button(root,text ='×',font = ('楷体',20),fg = "black",bd = 0.5,command = lambda:pressCompute('*'))
btnmul.place(x = 225,y = 230,width = 75,height = 55)
btnfactor = tkinter.Button(root,text ='x!',font = ('楷体',20),fg = "black",bd = 0.5,command = lambda:pressCompute('x!'))
btnfactor.place(x = 300,y = 230,width = 75,height = 55)
btnsub = tkinter.Button(root,text = '-',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('-'))
btnsub.place(x = 225,y = 285,width = 75,height = 55)
btnrecip = tkinter.Button(root,text = '1/x',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('1/x'))
btnrecip.place(x = 300,y = 285,width = 75,height = 55)
btnadd = tkinter.Button(root,text = '+',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('+'))
btnadd.place(x = 225,y = 340,width = 75,height = 55)
btnsin = tkinter.Button(root,text = 'sin',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('sin'))
btnsin.place(x = 300,y = 340,width = 75,height = 55)
btnequ = tkinter.Button(root,text = '=',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda :pressEqual('='))
btnequ.place(x = 225,y = 450,width = 75,height = 55)
btntan = tkinter.Button(root,text = 'tan',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda :pressCompute('tan'))
btntan.place(x = 300,y = 450,width = 75,height = 55)
btndiliver = tkinter.Button(root,text = '%',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('%'))
btndiliver.place(x = 225,y = 395,width = 75,height = 55)
btnpoint = tkinter.Button(root,text = '.',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('.'))
btnpoint.place(x = 150,y = 450,width = 75,height = 55)
btnroot = tkinter.Button(root,text = '√￣',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('√￣'))
btnroot.place(x = 0,y = 450,width = 75,height = 55)
btndeg = tkinter.Button(root,text = 'deg',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('deg'))
btndeg.place(x = 0,y = 505,width = 75,height = 55)
btnleft_bracket = tkinter.Button(root,text = '(',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressCompute('('))
btnleft_bracket.place(x = 75,y = 505,width = 75,height = 55)
btnlg = tkinter.Button(root,text = 'lg',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressCompute('lg'))
btnlg.place(x = 225,y = 505,width = 75,height = 55)
btnln = tkinter.Button(root,text = 'ln',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressCompute('ln'))
btnln.place(x = 300,y = 505,width = 75,height = 55)
btnright_bracket = tkinter.Button(root,text = ')',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda : pressCompute(')'))
btnright_bracket.place(x = 150,y = 505,width = 75,height = 55)
root.mainloop()
