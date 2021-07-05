def solution(m,n,puddles):
	load = [[0]*m for _ in range(n)]
	for i in puddles:
		load[i[1]-1][i[0]-1] = -1
	load[0][0] = 1
	for i in range(1,m):
		if load[0][i] != -1:
			load[0][i] = 1
		else:
			break
	for i in range(1,n):
		if load[i][0] != -1:
			load[i][0] = 1
		else:
			break
	for row in range(1,n):
		for col in range(1,m):
			if load[row][col] != -1:
				if load[row-1][col] != -1:
					load[row][col] += load[row-1][col]
				if load[row][col-1] != -1:
					load[row][col] += load[row][col-1]
	return load[n-1][m-1]%1000000007

print(solution(10,10,[]))