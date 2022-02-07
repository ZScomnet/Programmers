import sys
from collections import deque
input = sys.stdin.readline

def bfs(board,row,col,R,C):
	drop_point[col] = row
	down = [[row,col]]
	q = deque([[row,col]])
	board[row][col] = '.'
	drow,dcol = [-1,0,1,0],[0,1,0,-1]
	while q:
		r,c = q.popleft()
		for dr,dc in zip(drow,dcol):
			if 0 <= r+dr < R and 0 <= c+dc < C:
				if board[r+dr][c+dc] == 'x':
					if r+dr == R-1:
						for i in down:
							r,c = i
							board[r][c] = 'x'
						return
					down.append([r+dr,c+dc])
					q.append([r+dr,c+dc])
					board[r+dr][c+dc] = '.'
					drop_point[c+dc] = max(drop_point[c+dc],r+dr)
	drop = 101
	for i in range(len(down)):
		if board[i[0]+1][i[1]] != 'x':
			h = i[0]
			for j in range(drop_point[i]+1,R):
				if board[j][i] == "x":
					h = j
					break
			if h == drop_point[i]:
				drop = min(drop,R-h-1)
			else:
				drop = min(drop,h-drop_point[i]-1)
	for i in down:
		r,c = i
		board[r][c]	= '.'
	for i in down:
		r,c = i
		board[r+drop][c] = 'x'
		

	return

def solution(board,arrow,R,C):
	for i in range(len(arrow)):
		arrow[i] = R-arrow[i]
		if i%2 == 0:
			for j in range(C):
				if board[arrow[i]][j] == 'x':
					board[arrow[i]][j] = '.'
					if 0 <= arrow[i]-1:
						if board[arrow[i]-1][j] == 'x':
							bfs(board,arrow[i]-1,j,R,C)
					if 0 <= j+1 < C:
						if board[arrow[i]][j+1] == 'x':
							bfs(board,arrow[i],j+1,R,C)
					if 0 <= arrow[i]+1 < R:
						if board[arrow[i]-1][j] == 'x':
							bfs(board,arrow[i]-1,j,R,C)
					break
		else:
			for j in range(C-1,-1,-1):
				if board[arrow[i]][j] == 'x':
					board[arrow[i]][j] = '.'
					if 0 <= arrow[i]-1:
						if board[arrow[i]-1][j] == 'x':
							bfs(board,arrow[i]-1,j,R,C)
					if 0 <= j-1 < C:
						if board[arrow[i]][j-1] == 'x':
							bfs(board,arrow[i],j-1,R,C)
					if 0 <= arrow[i]+1 < R:
						if board[arrow[i]+1][j] == 'x':
							bfs(board,arrow[i]+1,j,R,C)
					break

	for i in board:
		print(''.join(i))

if __name__ == "__main__":
	R,C = map(int,input().split())
	board = []
	for _ in range(R):
		board.append(list(input())[:-1])
	N = int(input())
	arrow = list(map(int,input().split()))
	solution(board,arrow,R,C)