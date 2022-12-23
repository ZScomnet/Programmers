from collections import deque
import sys
input = sys.stdin.readline

def check(board,row,col):
	if board[row][col] == '.':
		return False
	R,C = len(board),len(board[0])
	q = deque([[row,col]])
	visited = [[0]*C for _ in range(R)]
	while q:
		r,c = q.popleft()
		visited[r][c] = 1
		for dr,dc in zip([-1,0,1,0],[0,1,0,-1]):
			if 0 <= r+dr < R and 0 <= c+dc < C:
				if board[r+dr][c+dc] == 'x' and visited[r+dr][c+dc] == 0:
					q.append([r+dr,c+dc])
					visited[r+dr][c+dc] = 1
					if r+dr == R-1:
						return False
	return True

def drop(board,row,col):
	R,C = len(board),len(board[0])
	q = deque([[row,col]])
	visited = [[0]*C for _ in range(R)]
	dropPoint = deque()
	while q:
		r,c = q.popleft()
		visited[r][c] = 1
		dropPoint.append([r,c])
		for dr,dc in zip([-1,0,1,0],[0,1,0,-1]):
			if 0 <= r+dr < R and 0 <= c+dc < C:
				if board[r+dr][c+dc] == 'x' and visited[r+dr][c+dc] == 0:
					q.append([r+dr,c+dc])
					visited[r+dr][c+dc] = 1
	minH = 1e9
	for i in dropPoint:
		r,c = i
		height = 0
		for dr in range(r+1,R):
			if board[dr][c] == '.':
				height += 1
			else:
				if visited[dr][c] == 1:
					height = 0
				break
		if height != 0:
			minH = min(minH,height)
	for i in dropPoint:
		r,c = i
		board[r+minH][c] = board[r][c]
		visited[r+minH][c] += 1
		visited[r][c] -= 1
	for i in dropPoint:
		r,c = i
		if visited[r][c] == 0:
			board[r][c] = '.'
	return board

def solution():
	R,C = map(int,input().split())
	board = []
	for _ in range(R):
		board.append(list(input().rstrip()))
	N = int(input())
	left = True
	h = list(map(int,input().split()))
	for i in h:
		if left:
			for col in range(C):
				if board[-i][col] == 'x':
					board[-i][col] = '.'
					left = False
					for drow,dcol in zip([-1,0,1],[0,1,0]):
						if 0 <= (R-i)+drow < R and 0 <= col+dcol < C:
							if check(board,(R-i)+drow,col+dcol):
								board = drop(board,(R-i)+drow,col+dcol)
								break
				if not left:
					break
			left = False
		else:
			for col in range(C-1,-1,-1):
				if board[-i][col] == 'x':
					board[-i][col] = '.'
					left = True
					for drow,dcol in zip([-1,0,1],[0,-1,0]):
						if 0 <= (R-i)+drow < R and 0 <= col+dcol < C:
							if check(board,(R-i)+drow,col+dcol):
								board = drop(board,(R-i)+drow,col+dcol)
								break
				if left:
					break
			left = True
	for i in board:
		print(''.join(i))

if __name__ == "__main__":
	solution()