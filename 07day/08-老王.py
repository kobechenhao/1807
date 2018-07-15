name = input("请输入一个名字")
money = float(input("请输入金钱"))

if name == "老王" and money > 1000:
    print("砖石王老五")
elif name == "老王" and money < 500:
    print("穷逼")
else:
    print("小康")

