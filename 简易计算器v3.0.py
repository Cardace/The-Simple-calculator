import tkinter

root = tkinter.Tk()
root.minsize(300,500)
root.title('calculator')



#界面布局
#显示面板
result = tkinter.StringVar()
result.set(0)                    #显示结果1，用于显示默认数字0
result2 = tkinter.StringVar()    #显示结果2，用于显示计算过程
result2.set('')

#显示板
label = tkinter.Label(root,font = ('楷体',20),bg = 'grey',bd ='9',fg = 'white',anchor = 'se',textvariable = result2)
label.place(width = 300,height = 140)
label2 = tkinter.Label(root,font = ('楷体',30),bg = 'grey',bd ='9',fg = 'white',anchor = 'se',textvariable = result)
label2.place(y = 140,width = 300,height = 90)


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
btnmul = tkinter.Button(root,text ='×',font = ('楷体',20),fg = "black",bd = 0.5,command = lambda:pressCompute('*'))
btnmul.place(x = 225,y = 230,width = 75,height = 55)
btnsub = tkinter.Button(root,text = '-',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('-'))
btnsub.place(x = 225,y = 285,width = 75,height = 55)
btnadd = tkinter.Button(root,text = '+',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('+'))
btnadd.place(x = 225,y = 340,width = 75,height = 55)
btnequ = tkinter.Button(root,text = '=',font = ('楷体',20),fg = ('red'),bd = 0.5,command = lambda :pressEqual())
btnequ.place(x = 225,y = 395,width = 75,height = 110)
btndiliver = tkinter.Button(root,text = '%',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressCompute('%'))
btndiliver.place(x = 0,y = 450,width = 75,height = 55)
btnpoint = tkinter.Button(root,text = '.',font = ('楷体',20),fg = ('black'),bd = 0.5,command = lambda:pressNum('.'))
btnpoint.place(x = 150,y = 450,width = 75,height = 55)

#临时存放输入数据的变量列表
lists = []                            #设置一个变量 保存运算数字和符号的列表
isPressSign = False                  #添加一个判断是否按下运算符号的标志,假设默认没有按下按钮
isPressNum = False

#判断数字函数
def pressNum(num):                   #设置一个数字函数 判断是否按下数字 并获取数字将数字写在显示版上
    global lists                     #全局化lists和按钮状态isPressSign
    global isPressSign
    if isPressSign == False:
        pass
    else:                            #重新将运算符号状态设置为否
        result.set(0)
        isPressSign = False

    #判断界面的数字是否为0
    oldnum = result.get()             #第一步
    if oldnum =='0':                 #如过界面上数字为0 则获取按下的数字
        result.set(num)
    else:                            #如果界面上的而数字不是0  则加上新按下的数字
        newnum = oldnum + num
        result.set(newnum)            #将按下的数字写到面板中


#相关特殊运算
def pressCompute(sign):
    global lists
    global isPressSign
    num = result.get()              #获取界面数字
    lists.append(num)               #保存界面获取的数字到列表中

    lists.append(sign)              #将按下的运算符号保存到列表中
    isPressSign = True

    if sign =='C':                #如果按下的是'AC'按键，则清空列表内容，# 讲屏幕上的数字键设置为默认数字0
        lists.clear()
        result.set(0)
    elif sign =='b':                 #如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
        a = num[0:-1]
        lists.clear()
        result.set(a)

#获取运算结果
def pressEqual():
    global lists
    global isPressSign


    curnum = result.get()           #设置当前数字变量，并获取添加到列表
    lists.append(curnum)

    computrStr = ''.join(lists)     #将列表内容用join命令将字符串链接起来
    endNum = eval(computrStr)       #用eval命令运算字符串中的内容
    result.set(endNum)              #将运算结果显示到text1
    result2.set(computrStr)         #将运算过程显示到text2
    lists.clear()                   #清空列表内容

root.mainloop()


