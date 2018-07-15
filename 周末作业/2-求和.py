start = 1
sum = 0
while start <100:
	temp = start % 2
	if temp ==1:
		sum = sum + start
	else:
		sum = sum - start
	start += 1
print(sum)
