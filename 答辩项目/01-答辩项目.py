import random
import time
print('欢迎使用QQ'.center(50,'*'))
print('请先注册你的QQ号'.center(50,' '))
while True:
	a = input('请输入你要注册的QQ号:')
	b = input('请输入你要注册QQ号的密码:')
	#判断是否输入正确
	if len(a) == 11 and a.startswith('1') == True and len(b)>=6:
		print('输入正确')
		break #如果输入正确,结束本次循环
	else:
		print('输入有误,请重新输入')

print('正在给你发送验证码...'.center(50,' '))
c = random.randint(1000,9999)
time.sleep(3) 
print('你的验证码为%d'%c)
while True:
	f =int(input('请输入你的验证码:'))
	if f == c :
		print('注册成功')
		break
	else :
		print('验证码输入有误,请重新输入')
print('请登录QQ'.center(50,'-'))
while True:
	d = input('请输入你的QQ号')
	e = input('请输入你的QQ密码')
	if d == a and b == e:
		print('登陆成功')
		break
	else :
		print('登录失败,请重新登录')
print('*'*50)
#注册登录完成,进入选择功能		
list=[] #定义空列表
def gn(): #功能函数
	print('1:添加好友'.center(50,' '))
	print('2:查找好友'.center(50,' '))
	print('3:修改好友'.center(50,' '))
	print('4:删除好友'.center(50,' '))
	print('5:显示全部好友及信息'.center(50,' '))
	print('6:退出系统'.center(50,' '))
def xz():#选择功能
	while True:
		a = int(input('请选择功能'))
		if a == 1:
			add() #调用添加函数
			print('-'*50)
		if a == 2:
			find() #调用查找函数
			print('-'*50)
		if a == 3:
			xg() #调用修改函数
			print('-'*50)
		if a == 4:
			sc() #调用删除函数
			print('-'*50)
		if a == 5:
			xs() #调用显示全部内容函数
			print('-'*50)
		if a == 6:
			print('退出成功,欢迎下次使用'.center(50,'*'))
			break 
def add():#添加
	l = {}
	while True:
		b = input('请输入要添加好友姓名')
		#判断添加名字是否符合以下条件,符合结束循环,否则重新输入
		if len(b) <=4: 
			break
		else:
			print('输入有误,请重新输入') 
	while True:	
		c = input('请输入要添加好友的手机号')
		#判断添加手机号是否符合以下条件,符合结束循环,否则重新输入
		if len(c) ==11 and c.startswith('1'):
			break
		else:
			print('输入有误,请重新输入')
	while True:
		d = input('请输入要添加好友的地址')
		#判断添加地址是否符合以下条件,符合结束循环,否则重新输入
		if len(d) <=6:
			break
		else:
			print('输入有误,请重新输入')
#把内容添加到字典
	l['b']=b
	l['c']=c
	l['d']=d
	list.append(l) #添加到列表
	print('添加成功')

def find():#查找
	b1 = input('请输入你要查找的姓名')
	flag = False  #假设里面没有要查找的名字
	for i in list: #把字典从列表里遍历出来
		if i['b'] == b1: #如果我要查找的名字在字典里,打印内容
			print('姓名:%s\n微信号:%s\n地址:%s'%(i['b'],i['c'],i['d']))
			flag = True	#表示找到了
			break
	if flag == False: 
		print('没有你要查找的姓名')



def xg():#修改
	b2 = input('请输入要修改的名字')
	flag = False #假设里面没有要修改的名字
	for i in list:
		while True:
			if i['b'] == b2:
				flag = True
				print('1:请输入要修改的名字')
				print('2:请输入要修改的手机号')
				print('3:请输入要修改的地址')
				print('4:退出修改系统')
				j = int(input('请选择要修改的功能'))
				if j == 1:
					b = input('请输入新的名字')
					i['b'] = b
					print('修改成功')
					break
				
				elif j == 2:
					c = input('请输入新的手机号')
					i['c'] = c
					print('修改成功')
					break
				elif j == 3:
					d = input('请输入新的地址')
					i['d'] = d
					print('修改成功')
					break
				elif j == 4:
					print('退出成功')
					break
			elif flag == False:
				print('没有要修改的名字')
				break	


def sc():#删除
	b3 = input('请输入你要删除的名字')
	for i in list:
			for position,i in enumerate(list):
					list.pop(position) #删除字典所在列表的索引值
					print('删除成功')




def xs():#显示所有内容
	print('名字\t手机号\t\t地址')
	for i in list:
		print(i['b']+'\t'+i['c']+'\t'+i['d'])




		
gn() #调用功能函数
xz() #调用选则功能函数	
