account = 123456
passwd = "123123"
a = int(input("请输入你的账户"))
p = input("请输入你的密码")
if a == account and p == passwd:
	print("登陆成功")
if a != account:
	print("账户错误")
if p != passwd:
	print("密码错误")
