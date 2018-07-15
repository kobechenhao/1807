name = input("请输入名字")
age = input("请输入年龄")
sex = input("请输入性别")
height = float(input("请输入身高"))
come = input("请输入来自哪")
#print(name,age,sex,height,come)

'''
print(name)
print(age)
print(sex)
print(height)
print(come)
'''

#格式化输出
#%s 占位字符串
#%f 占位浮点数 保留两位小数%.02f
#%d 占位整数
print("我的名字是%s"%name)#单个占位符

print("我的名字是%s,我的年龄是%s,我的性别是%s,我的身高是%0.2f,我来自%s"%(name,age,sex,height,come))








