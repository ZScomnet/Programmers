from collections import deque

def drop(board):
	for col in range(8):
		if board[7][col] == '#':
			board[7][col] = '.'
	for row in range(7,0,-1):
		for col in range(8):
			if board[row-1][col] == '#':
				board[row][col] = '#'
				board[row-1][col] = '.'


def solution():
	q = deque()
	q.append([7,0])
	board = []
	for _ in range(8):
		board.append(list(input()))
	while q:
		next_q = deque()
		visited = [[0]*8 for _ in range(8)]
		while q:
			row,col = q.popleft()
			if row == 0 and col == 7:
				return 1
			if board[row][col] == '#':
				continue
			for drow,dcol in zip([-1,-1,-1,0,0,0,1,1,1],[-1,0,1,-1,0,1,-1,0,1]):
				if 0 <= row+drow < 8 and 0 <= col+dcol < 8:
					if visited[row+drow][col+dcol] == 0 and board[row+drow][col+dcol] == '.':
						visited[row+drow][col+dcol] = 1
						next_q.append([row+drow,col+dcol])
		drop(board)
		q = next_q
	return 0

if __name__ == "__main__":
	print(solution())