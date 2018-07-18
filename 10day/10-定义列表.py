list = ["小杨是傻逼","小刘是傻逼","小马是帅哥","小胡"]
list1 = ["1","2","3","4"]
list.append(list1)
print(list)
list.extend(list1)
print(list)
for i in list:
	print(i)

