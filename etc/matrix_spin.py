def spin(matrix,query,r,c):
	result = 1000001
	data = []
	data.append(matrix[query[0]-1][query[3]-1])
	result = min(result,matrix[query[0]-1][query[3]-1])
	for i in range(query[3]-1,query[1]-1,-1):
		result = min(result,matrix[query[0]-1][i-1])
		matrix[query[0]-1][i] = matrix[query[0]-1][i-1]

	data.append(matrix[query[2]-1][query[3]-1])
	result = min(result,matrix[query[2]-1][query[3]-1])
	for i in range(query[2]-1,query[0]-1,-1):
		result = min(result,matrix[i-1][query[3]-1])
		matrix[i][query[3]-1] = matrix[i-1][query[3]-1]
	matrix[query[0]][query[3]-1] = data[0]

	data.append(matrix[query[2]-1][query[1]-1])
	result = min(result,matrix[query[2]-1][query[1]-1])
	for i in range(query[1]-1,query[3]-1):
		result = min(result,matrix[query[2]-1][i+1])
		matrix[query[2]-1][i] = matrix[query[2]-1][i+1]
	matrix[query[2]-1][query[3]-2] = data[1]

	for i in range(query[0]-1,query[2]-1):
		result = min(result,matrix[i+1][query[1]-1])
		matrix[i][query[1]-1] = matrix[i+1][query[1]-1]
	matrix[query[2]-2][query[1]-1] = data[2]

	return result


def solution(rows,columns,queries):
	answer = []
	matrix = []
	for i in range(rows):
		matrix.append([columns*i+j for j in range(1,columns+1)])
	for query in queries:
		answer.append(spin(matrix,query,rows,columns))
		for i in matrix:
			print(i)
		print()

	return answer

if __name__ == "__main__":
	print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))