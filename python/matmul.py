


a = [[2,3,4,5],
	[1,1,1,2]]
b = [[1,1],[2,1],[3,1],[4,1]]



def mat_mul(a,b):
	a_row = len(a)
	a_col = len(a[0])
	b_row = len(b)
	b_col = len(b[0])
	if a_col != b_row:
		print("mulitplication not possible")
	c = []
	for i in range(a_row):
		tmp = []
		for j in range(b_col):
			tmp.append(0)
		c.append(tmp)
	print(c)

	for i in range(a_row):
		for j in range(a_col):
			for k in range(b_col):
				c[i][k]+=a[i][j]*b[j][k]
	print(c)



mat_mul(a,b)