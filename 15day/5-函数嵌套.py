list = []
def showError(msg):
	print("输入有误，请重新输入"+msg)

def isNum():
	if num.isdigit():
		return Ture
	else:
		return False
def add():
	stu = {}
	while True:
		name = input("请输入姓名")
		if len(name) >= 2 and len(name) <= 4:
			stu["name"] = name
			break
		else:
			showError("学生姓名必须大于2小于4")
	while True:
		age = input("请输入年龄")
		if isNum(age):
			else:
				print("输入有误")
				continue
		if age > 1 and age < 130:
			stu["age"] = age
			break
		else:
			showError("年龄必须大于1小于130")
	list.append(stu)
	print(list)
def find():
	name = input("请输入查找的姓名")
	for stu in list:
		if stu["name"] == name:
			print("学生姓名:%s\n学生年龄:%d"%(stu["name"],stu["age"]))
			break
	

def change():
	name = input("请输入修改的名字")
	for stu in list:
		if stu["name"] == name:
			print("1.修改名字")
			print("2.修改年龄")
			num = int(input("请选择功能"))
			if num == 1:
				name = input("请输入新的名字")
				stu["name"] = name
			elif num == 2:
				age = int(input("请输入新的年龄"))
				stu["age"] = age
			break

def delete():
	name = input("请选择删除的名字")
	for stu in list:
		if stu["name"] == name:
			list.remove(stu)
			print("删除成功")
			break

def print_list():
	print("姓名        年龄")
	for stu in list:
		print("%s        %d"%stu(["name"],stu["age"]))

def print_menu():
	print("欢迎来到学生管理系统".center(30,""))
	while True:
		print("1.添加学生信息")
1		print("2.查看学生信息")
		print("3.修改学生信息")
		print("4.删除学生信息")
		print("5.打印学生信息")
		print("6.退出管理系统")
		input_info()
def input_info():
	num = int(input("请选择序号功能"))
	if isNum(num):
		num = int(num)
	else:
		print("输入有误")
	if num == 1:
		add()
	elif num == 2:
		find()
	elif num == 3:
		change()
	elif num == 4:
		delete()
	elif num == 5:
		print_list()
	elif num == 6:
		exit()
print_menu()
