account = "mch"
password = "123456"
i = 0
while i < 3:
	user_name = input("请输入用户名")
	user_password = input("请输入密码")
	if user_name == account and user_password == password:
		print("登录成功")
		number = int(input("请选择0:ADC 1:肉 2:法师"))
		if number == 0:
			print("鲁班")
		elif number == 1:
			print("陈咬金")
		elif number == 2:
			print("王昭君")
	else:
		if i!=2:
			print("输入错误 请重新输入")
		else:
			print("账号被冻结")
	i+=1
		
