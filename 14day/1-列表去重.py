list = [1,2,3,4,4,5,6,6,7,7,8]
list1 = []
for i in list:
	if i not in list1:
		list1.append(i)
print(list1)
