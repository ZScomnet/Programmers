import sys
input = sys.stdin.readline

def multi(matrixA,matrixB,N):
	result = [[0]*N for _ in range(N)]
	for row in range(N):
		for col in range(N):
			for i in range(N):
				result[row][col] += matrixA[row][i] * matrixB[i][col]

	for row in range(N):
		for col in range(N):
			result[row][col] %= 1000
	return result

def print_matrix(matrix):
	for row in matrix:
		for col in row:
			print(col,end=" ")
		print()

if __name__ == "__main__":
	N,B = map(int,input().split())
	matrix = []
	for _ in range(N):
		line = list(map(int,input().split()))
		matrix.append(line)

	now = 0
	while B != 0:
		if B % 2 == 1:
			if now == 0:
				now = matrix
			else:
				now = multi(matrix,now,N)
		B = B//2
		matrix = multi(matrix,matrix,N)
	for row in range(N):
		for col in range(N):
			now[row][col] %= 1000
	print_matrix(now)