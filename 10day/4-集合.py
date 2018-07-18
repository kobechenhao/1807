#list

#home = ["老王","老宋","老刘","小杨",1,1.2,True]#定义>一个列表
#进房间----------------添加

home1 = ["老王"]
#home1.append("老宋")#添加老宋进来
#print(home1)

home1.insert(0,"老宋")#插队
print(home1)
#走出房间-------------删除
#home1.pop()
#print(home1)

#home1.pop(0)#谁在0号谁走  根据座位号删除
#print(home1)


#home1.remove("老宋")#根据名字删
#print(home1)
#根据座位号查找
print(home1[0])

#修改
home1[0] = "杨昕義"
print(home1)
