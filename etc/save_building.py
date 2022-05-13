def solution(board,skill):
	R,C = len(board),len(board[0])
	new_board = [[0]*(C+1) for _ in range(R+1)]
	for i in skill:
		stat,r1,c1,r2,c2,degree = i
		if stat == 1:
			degree *= -1
		new_board[r1][c1] += degree
		new_board[r2+1][c2+1] += degree
		new_board[r1][c2+1] -= degree
		new_board[r2+1][c1] -= degree

	for row in range(R):
		for col in range(1,C):
			new_board[row][col] += new_board[row][col-1]

	for col in range(C):
		for row in range(1,R):
			new_board[row][col] += new_board[row-1][col]

	answer = 0

	for row in range(R):
		for col in range(C):
			if new_board[row][col] + board[row][col] > 0:
				answer += 1

	return answer

if __name__ == "__main__":
	print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))