def clum1(x,y,z):
	ret =z(x,y)
	return ret
ret = clum1(1,2,lambda x,y:x*y)
print(ret)

