def block_down(row,col,board):
	if board[row][col] == 0:
		for r in range(row,-1,-1):
			if board[r][col] != 0:
				board[row][col] = board[r][col]
				board[r][col] = 0
				break

def solution(m,n,board):
	cnt = 1
	for i in range(len(board)):
		board[i] = list(board[i])

	answer = 0
	while cnt != 0:
		cnt = 0
		block_point = set()
		srow = 0
		scol = set()
		for row in range(m-1):
			for col in range(n-1):
				if board[row][col] == board[row+1][col] == board[row][col+1] == board[row+1][col+1] != 0:
					block_point.add((row,col))
					block_point.add((row+1,col))
					block_point.add((row+1,col+1))
					block_point.add((row,col+1))
					cnt += 1
					srow = max(srow,row+1)
					scol.add(col)
					scol.add(col+1)
		for point in block_point:
			board[point[0]][point[1]] = 0
			answer += 1
		for row in range(srow,0,-1):
			for col in scol:
				block_down(row,col,board)

	return answer

print(solution(6,6,	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))