'''
d = {"name":" 老王","sex":"男","mz":"汉","brithday","2000年6月27日","address":"山西"}
#添加或修改
d["age"] = 18
print(d)
d["name"] = "老宋"


#删除
d.pop("name")
print(d)

d["sex"]
#查找
print(d["sex"])
'''
'''
d["name"] = "xxx"

for i in d:
	print(i)
	print(d[i])
'''
'''
for i in d.keys():
	print(i)
	print(d[i])
'''
'''
for i in d.valuse():
	print(i)
'''

'''
for k,v in d.items():
	print(k)
	print(v)
'''

#特殊的几个方法
d1 = {"name":"老王","age":12}
#print(d["name"])
#print(d.git("name"))

#d["name"] = "老宋"
#d.setdefault("name1","老宋")
d1 = {"sex":"男"}
d.update(d1)
print(d)




