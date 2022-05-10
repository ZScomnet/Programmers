dy,dx = [-1,0,1,0],[0,1,0,-1]

def check_out_of_range(R,C,row,col,drow,dcol):
	if 0 <= row+drow < R and 0 <= col+dcol < C:
		return False
	else:
		return True

def search(board,aloc,bloc,now):
	answer = 0
	if now == "A":
		row,col = aloc
		if board[row][col] == 0:
			return 0
		for drow,dcol in zip(dy,dx):
			if check_out_of_range(len(board),len(board[0]),row,col,drow,dcol):
				continue
			elif board[row+drow][col+dcol] == 0:
				continue
			board[row][col] = 0
			result = search(board,[row+drow,col+dcol],bloc,"B")+1
			board[row][col] = 1

			if answer % 2 == 0 and result % 2 == 1:
				answer = result
			elif answer % 2 == 1 and result % 2 == 1:
				answer = min(answer,result)
			elif answer % 2 == 0 and result % 2 == 0:
				answer = max(answer,result)
	else:
		row,col = bloc
		if board[row][col] == 0:
			return 0
		for drow,dcol in zip(dy,dx):
			if check_out_of_range(len(board),len(board[0]),row,col,drow,dcol):
				continue
			elif board[row+drow][col+dcol] == 0:
				continue
			board[row][col] = 0
			result = search(board,aloc,[row+drow,col+dcol],"A")+1
			board[row][col] = 1

			if answer % 2 == 0 and result % 2 == 1:
				answer = result
			elif answer % 2 == 1 and result % 2 == 1:
				answer = min(answer,result)
			elif answer % 2 == 0 and result % 2 == 0:
				answer = max(answer,result)
	return answer

def solution(board,aloc,bloc):
	return search(board,aloc,bloc,"A")

if __name__ == "__main__":
	print(solution(	[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))