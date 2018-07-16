import random
'''
1---石头
2---剪刀
3---布
'''
for i in range(1,11):
	pc = random.randint(1,3)
	player = int(input("请输入1.石头,2.剪刀,3.布"))
	if (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
		print("玩家赢")
	elif pc == player:
		print("平局")
	else:
		print("电脑赢")

