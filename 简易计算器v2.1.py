from tkinter import *
import random
root = Tk()

class Calculator():
	
	# 设置窗口大小
	def __init__(self,height,width,title):
		root.maxsize(height, width)
		root.minsize(height, width)
		root.title(title)
		# 设置初始透明度
		self.nums = 1
		# 设置第一个数
		self.previous = ''
		# 设置运算方法
		self.operation = ''
		# 设置第二个数
		self.current = ''
		# 设置是否按下运算符
		self.istrue = False
		# 设置初始颜色
		self.color = ''
		#是否已经运算
		self.click = False
		#设置计算公式
		# self. result = self.previous + self.operation + self.current
		#设置结果集
		self.result =''
	
	
	# 设置窗口颜色
	root_show = Frame(width=300, height=30)
	
	
	def set_label(self):
		# 设置窗口颜色
		root_show = Frame(width=300, height=30)
		# 编辑2个label
		head_top = Label(root_show, bg='#EEE9E9', fg='#FF8C00', text='Hello World', font=("微软雅黑", 18), anchor='w', width=100)
		top_label = Label(root_show, bg='#EEE9E9', fg='#FF3030', text='0', font=("微软雅黑", 20), anchor='se', height=2,
		                  borderwidth=20, width=100)
		self.top = top_label
		head_top.pack()
		top_label.pack()
		root_show.pack()
	
	def set_span(self):
		# 设置键盘和主界面
		frame_body = Frame(width=350, height=500, bg='#cccccc')
		
		button_c = Button(frame_body, text='C', bd='4', width=6, height=2, font=('微软雅黑', 13), bg='#C1CDC1',
		                  fg='#000000', command=lambda:self.fun_c()).grid(row=0, column=0)

		button_ce = Button(frame_body, text='CE', bd='4', width=6, height=2, font=('微软雅黑', 13), bg='#787878',
		                   fg='#ffffff', command=lambda: self.fun_ce()).grid(row=0, column=1)
		button_del = Button(frame_body, text='←', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#787878',
		                    fg='#ffffff', command=lambda: self.fun_t()).grid(row=0, column=2)
		button_minus = Button(frame_body, text='±', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#787878',
		                   fg='#ffffff', command=lambda: self.fun_minus()).grid(row=0, column=3)
		button_1 = Button(frame_body, text='1', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=1, column=0)
		button_2 = Button(frame_body, text='2', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=1, column=1)
		button_3 = Button(frame_body, text='3', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=1, column=2)
		button_div = Button(frame_body, text='/', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                    fg='#ffffff').grid(row=1, column=3)
		button_4 = Button(frame_body, text='4', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=2, column=0)
		button_5 = Button(frame_body, text='5', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=2, column=1)
		button_6 = Button(frame_body, text='6', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=2, column=2)
		button_mul = Button(frame_body, text='*', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                      fg='#ffffff').grid(row=2, column=3)
		button_7 = Button(frame_body, text='7', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=3, column=0)
		button_8 = Button(frame_body, text='8', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=3, column=1)
		button_9 = Button(frame_body, text='9', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=3, column=2)
		button_plus = Button(frame_body, text='+', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                    fg='#ffffff').grid(row=3, column=3)
		button_point = Button(frame_body, text='.', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                     fg='#ffffff').grid(row=4, column=0)
		button_0 = Button(frame_body, text='0', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff').grid(row=4, column=1)
		button_power = Button(frame_body, text='^', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
							 fg='#ffffff').grid(row=4, column=2)
		button_left = Button(frame_body, text='(', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                     fg='#ffffff').grid(row=5, column=2)
		button_right = Button(frame_body, text=')', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                     fg='#ffffff').grid(row=5, column=3)
		button_eq = Button(frame_body, text='=', bd='4', width=13, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
						   fg='#ffffff').grid(row=5, column=0,columnspan=2)
		button_sub = Button(frame_body, text='-', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
						   fg='#ffffff').grid(row=4, column=3)
		self.body = frame_body
		# 显示主页面
		frame_body.pack()

	def bracket_left(self):
		if self.operation:
			self.current = self.current + '('
			self.show('current')
		else:
			self.previous = self.previous+'('
			self.show('previous')

	def bracket_right(self):
		if self.operation:
			self.current = self.current + ')'
			self.show('current')
		else :
			self.previous = self.previous+')'
			self.show('previous')
	# 点方法
	def func_point(self):
		if self.operation:
			if self.current.find('.') == -1 :
				self.current = self.current + '.'
				self.show('current')
		else :
			if self.previous.find('.') == -1:
				self.previous = self.previous+'.'
				self.show('previous')
	
	
	#正负方法
	def fun_minus(self):
		if self.operation  :
			if   (self.current == '' or  str(self.current)[0] == '0'):
				return
			
			if str(self.current)[0] == '-' :
				self.current = str(self.current)[1:]
			else:
				self.current = '-' + str(self.current)
			self.show('current')
		else:
			if (self.previous == '' or  str(self.previous)[0] =='0') :
				return
			if str(self.previous)[0] == '-':
				self.previous = str(self.previous)[1:]
			else :
				self.previous = '-' + str(self.previous)
			self.show('previous')
		return

	#退格方法
	def fun_t(self):
		
		if self.click:
			return
		
		if self.operation :
			#如果长度有2个多
			if len(str(self.current)) >=2 :
				self.current = self.current[0:-1]
			#反之只有1个长度
			else :
				self.current = '0'
			show = 'current'
		else :
			if len(str(self.previous)) >=2 :
				self.previous = self.previous[0:-1]
			else :
				self.previous = '0'
			show = 'previous'
		self.show(show)
		
	#ce 方法
	def fun_ce(self):
		if self.operation:
			self.current = '0'
			show = 'current'
		else :
			self.previous = '0'
			show = 'previous'
		self.show(show)
	
	#c方法
	def fun_c(self):
		self.previous = '0'
		self.operation = ''
		self.current = ''
		self.click = False
		self.show('previous')
		return
			
	#运算方法
	def func_operation(self,text):

		# 判断是否是运算状态
		if self.click:
			#如果计算完后再次点击运算符号
			if text in '+-*/^':
				self.previous = str(self.result)
				self.operation = text
				self.current = ''
				self.click = False
				self.show('previous')
				return
			#判断是不是等号 text 为等号会报错
			if text =='=':
				text = self.operation
			#除数不能为0
			if text =='/' and str(self.current) =='0':
				self.result = '0'
				self.show('*=')
				return
			
			
			result = str(self.result) +  text +  str(self.current)
			#处理结果 返回结果集
			self.result = eval(result)
			#解决余数为浮点数 1.0的 情况
			if self.result and  str(self.result)[-1] == '0'   and str(self.result)[-2] == '.':
				self.result = int(self.result)
			self.show('*=')
			return
		

			
		#如果直接点击运算符号
		if self.previous =='' and  self.current =='' and text :
			self.previous='0'
			self.operation =text
			self.current =''
			self.show('operation')
			return
		#第一个数字填写后 才能填写运算符号
		if self.previous != '':
			#正常运算 添加运算符
			if text in '+-*/^' and  self.operation == '' and self.current == '' :
				if text == '^':
					text = '**'
				self.operation = text
				self.show('operation')
				return
			#还没运算完 在进行运算符操作
			elif  text != '=' and self.operation :
				if self.operation == '/' and str(self.current) == '0':
					self.fun_c()
				
				if len(str(self.current)) < 1:
					self.operation = text
					self.show('operation')
					return
				if str(self.current)[0] == '(':
					self.current
				strs = str(self.previous) + str(self.operation) + str(self.current)
				strs = eval(strs)
				if strs and  str(strs)[-1] == '0' and str(strs)[-2] == '.':
					strs = int(strs)
				self.previous = "%g"%strs
				self.operation = text
				self.current = ''
				self.show('operation')
				return



		#如果2个运算数字都存在 则开始进行运算
		if self.previous and self.current:
			#除数不能为0
			if self.current =='0' and self.operation == '/':
				self.result = '0'
				self.show('*=')
				# self.click = True
				return
			#如果运算等式成立 按等于号
			if text =='=':
				strs = str(self.previous) + str(self.operation) + str(self.current)
				self.result = eval(strs)
				if self.result and str(self.result)[-1] == '0' and str(self.result)[-2] == '.':
					self.result = int(self.result)
				self.show('')
				self.click = True
				return


	#鼠标移入方法
	def Mouse_Entry(self,e):
		global colo
		colo = e.widget['bg']
		nums = str(random.randint(0, 1000000))
		if len(nums) != '6':
			nums = nums.ljust(6, str(random.randint(0, 9)))
		e.widget['bg'] = '#' + nums
	
	#鼠标移出事件
	def Mouse_Uot(self,e):
		global colo
		e.widget['bg'] = colo
		pass
	
	#鼠标滚轮事件
	def Mouse_on(self,e):
		if e.delta == -120 and self.nums > 0.11:
			self.nums -= 0.1
			root.attributes("-alpha", self.nums)  # 窗口透明度70 %
		elif e.delta == 120 and self.nums < 1:
			self.nums += 0.1
			root.attributes("-alpha", self.nums)
		
	# 显示
	def show(self,sign):
		show = ''
		if sign =='previous':
			self.top['text'] = str(self.previous)
		elif sign == 'operation':
			self.top['text'] = str(self.previous) + '\n' + str(self.operation)
		elif sign == 'current':
			self.top['text'] = str(self.previous) + self.operation + '\n' + str(self.current)
		elif sign == '*=':
			
			result = self.result
			if len(str(show)) >18:
				show = str("%g" %result)
				

			self.top['text'] = result
		else:
			result = self.result
			if len(str(result)) > 18:
				result = str("%g" % result)
				
			show = str(self.previous) + str(self.operation) + str(self.current) + '=' + '\n' +str(result).rjust(9,' ')
			self.top['text'] = result
			
	#鼠标点击事件
	def Mouse_click(self,e):
		#获取点击的值
		text = e.widget['text']
		
		# 输入的值最高为15为数
		if len(str(self.previous)) > 16 or len(str(self.current)) > 16:
			if self.operation:
				self.current = "%g" % float(self.current)
			else:
				self.previous = "%g" % float(self.previous)
			
			pass
		# 括号方法
		if text == '(':
			self.func_bracket_left()
			return
		if text == ')':
			self.func_bracket_right()
			return
		# 运算方法
		if text in '+-*/=^':
			self.func_operation(text)
			return
		#C 方法
		if text == 'C':
			self.fun_c()
			return

		#CE 方法
		if text == 'CE':
			self.fun_ce()
			return

		#小数点方法
		if text =='.' :
			self.func_point()
			return

		#退格方法
		if text == '←':
			self.fun_t()
			return
		#正负方法
		if text  == '±':
			self.fun_minus()
			return

		#如果在新点一个数字 则取消运算状态
		if self.click and text not in '+-*/=^':
			self.click = False
			self.previous = ''
			self.current = ''
			self.operation = ''

			
		#如果输入的不是数字键 则暂停
		if text not in '1234567890':
			return
		
		
		
		#不能出现连续以0开头的数值
		if(str(self.current)[0:1] == '0' or str(self.previous)[0:1] =='0') and self.operation ==''  :
			if self.operation :
				self.current = text
				show = 'current'
			else :
				self.previous = text
				show = 'previous'
			self.show(show)
			return
		elif self.current[0:1] == '0'  and   self.operation !='' :
			self.current = text
			show = 'current'
			self.show(show)
			return
		
		
		#如果显示的是0 和输入的是0
		if  self.top['text'] == '0' and text != '0' :
			if self.operation :
				self.current =text
				show = 'current'
			else :
				self.previous = text
				show = 'previous'
			self.show(show)
			return
		
		#如果有标点符号 则显示 第二个数字 反之 显示第一个
		if self.operation :
			self.current += text
			si = 'current'
		else:
			self.previous += text
			si ='previous'
		self.show(si)
		
	

	#调用事件
	def call_fun(self):
		self.body.bind_class('Button', '<Enter>', self.Mouse_Entry)
		self.body.bind_class('Button', '<Leave>', self.Mouse_Uot)
		self.body.bind_class('Button', '<Button-1>', self.Mouse_click)
		root.bind('<MouseWheel>', self.Mouse_on )

		
		
		
if __name__ == '__main__':
	calculator =  Calculator(320,600,'计算器')
	calculator.set_label()
	calculator.set_span()
	calculator.call_fun()
	root.mainloop()