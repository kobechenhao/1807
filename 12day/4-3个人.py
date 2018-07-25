l = []
for i in range(3):
	d = {}
	name = input("请输入姓名")
	age = input("请输入年龄")
	sex = input("请输入性别")
	d["name"] = name
	d["age"] = age
	d["sex"] = sex
	l.append(d)

print(l)
#l = [{},{},{}]
#i = {}
for i in l:
	for k,v in i:
		print(k,v)
