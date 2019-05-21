def int_lst(x):
	y = []
	for i in x:
		i = int(i)
		y.append(i)
	return y
	
matrix = []
while True:
	lst = [n for n in input().split()]
	if lst != ['end']:
		lst = int_lst(lst)
		matrix.append(lst)
	else:
		break
rows = len(matrix)
cols = len(matrix[0])
a = [[0 for j in range(cols)] for i in range(rows)]
for i in range(rows):
	for j in range(cols):
		if i + 1 < rows and j + 1 < cols:
			a[i][j] = matrix[i][j-1]+matrix[i][j+1]+matrix[i-1][j]+matrix[i+1][j]
		elif i + 1 >= rows and j + 1 < cols:
			a[i][j] = matrix[i][j-1]+matrix[i][j+1]+matrix[i-1][j]+matrix[0][j]
		elif i + 1 < rows and j + 1 >= cols:
			a[i][j] = matrix[i][j-1]+matrix[i][0]+matrix[i-1][j]+matrix[i+1][j]
		else:
			a[i][j] = matrix[i][j-1]+matrix[i][0]+matrix[i-1][j]+matrix[0][j]
for t in a:
	for r in t:
		print (r, end=" ")
	print()
