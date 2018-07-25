students = []
print("欢迎来到学生管理系统")
print("1:添加学生信息")
print("2:查找学生信息")
print("3:修改学生信息")
print("4:删除学生信息")
print("5:打印全部学生")
print("6:退出系统")
while True:
	num = int(input("请选择功能"))
	if num == 1:
		stu = {}
		name = input("请输入姓名:")
		phone = int(input("请输入电话:"))
		sex = input("请输入性别:")
		age = int(input("请输入年龄:"))
		stu["name"] = name
		stu["phone"] = phone
		stu["sex"] = sex
		stu["age"] = age
		students.append(stu)
		print(students)
	elif num == 2:
		name = input("请输入学生名字")
		for stu in students:
			if stu["name"] == name:
				print("学生名字是:%s\n学生电话:%d\n学生性别:%s\n学生年龄:%d\n"%(stu["name"],stu["phone"],stu["sex"],stu["age"]))
				print("1:修改名字")	
				print("2:修改电话")
				print("3:修改性别")
				print("4:修改年龄")
				num = int(input("请输入修改序号"))
				if num == 1:
					name = input("请输入新的名字")
					stu["name"] = name
				elif num == 2:
					phone = int(input("请输入新的电话"))
					stu["phone"] = phone
				elif num == 3:
					sex = input("请输入新的性别")
					stu["sex"] = sex
				elif num == 4:
					age = int(input("请输入新的年龄"))
					stu["age"] = age
				print("修改成功")
				break 
		print("查找学生信息")
	elif num == 3:
		print("修改学生信息")
	elif num == 4:
		name = input("请输入学生姓名")
		for stu in students:
			if stu["name"] == name:
				students.remove(stu)
				print("删除成功")
	elif num == 5:
		print("打印全部信息")
		print("姓名      年龄      ")
		for stu in students:
		print
	elif num == 6:
		print("退出系统")
		break

