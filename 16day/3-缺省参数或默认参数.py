def eat(a,b,c="水"):
	print(a)
	print(b)
	print(c)

eat("大米","蒜台炒肉丝","水煮肉片")


#定义函数,计算一个求和,如果不传默认求1-100的和 如果传的就是传1-传的那个数字的和

def MySum(a,b=100):
	sum = 0#局部变量
	for i in range(a,b=1):
		sum = sum +i
	return sum

ret = MySum(1)
print(ret)















