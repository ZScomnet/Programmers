from collections import deque

def solution(rectangle,characterX,characterY,itemX,itemY):
	board = [[0] * 101 for _ in range(101)]
	characterX,characterY = characterX*2,characterY*2
	itemX,itemY = itemX*2,itemY*2
	for i in rectangle:
		sr,sc,fr,fc = i
		sr,sc,fr,fc = sr*2,sc*2,fr*2,fc*2
		for row in range(sr,fr+1):
			for col in range(sc,fc+1):
				if (row == sr or row == fr or col == sc or col == fc) and board[row][col] != -1:
					board[row][col] = 1
				else:
					board[row][col] = -1
	q = deque()
	q.append([characterX,characterY])
	d = [(-1,0),(0,1),(1,0),(0,-1)]
	cnt = 0
	while q:
		next_q = deque()
		while q:
			row,col = q.popleft()
			board[row][col] = -1
			if row == itemX and col == itemY:
				return cnt // 2
			for i in d:
				drow,dcol = i
				if 0 <= row+drow < 51 and 0 <= col+dcol < 51:
					if board[row+drow][col+dcol] == 1:
						next_q.append([row+drow,col+dcol])
		q = next_q
		cnt += 1

if __name__ == "__main__":
	print(solution([[1, 1, 3, 3]], 1, 1, 1, 2))