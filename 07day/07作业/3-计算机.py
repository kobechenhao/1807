x = float(input("请输入值数"))
y = float(input("请输入值数"))
z = input("请输入+,-,*,/")
 
if z == "+":
    print("x+y的值为%.02f"%(x+y))
elif z == "-":
    print("x-y的值为%.02f"%(x-y))
elif z == "*":
    print("x*y的值为%.02f"%(x*y))
elif z == "/":
	if y == 0:
		print("不合法")
	else:
		print("x/y的值为%.02f"%(x/y))
