list = [1,2,3,4,5,6,87,99]
'''
num = int(input("请输入一个数"))
if num in list:
	position = list.index(num)
	print("索引是%d"%position)
	print(list)
else:
	print("不在列表中")
'''
'''
if num in list:
	for p,i in enumerate(list):
		if i == num:
			print("索引是%d"%p)
			print(list)
			break
else:
	print("不存在")
'''
p = 0
if num in list:
	fpr i in list:
		if i == num:
			print("索引时%d"%p)
			print(list)
			break
		p+=1
else:
	print("不存在")
