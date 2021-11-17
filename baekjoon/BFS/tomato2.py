import sys
from collections import deque

input = sys.stdin.readline

def solution(board,x,y,z):
	cnt = 0
	answer = 0
	q = deque()
	drow,dcol,dz = [-1,0,1,0,0,0],[0,1,0,-1,0,0],[0,0,0,0,1,-1]
	for h in range(z):
		for row in range(y):
			for col in range(x):
				if board[h][row][col] == 0:
					cnt += 1
				elif board[h][row][col] == 1:
					q.append([h,row,col])

	while q:
		next_q = deque()
		while q:
			h,row,col = q.popleft()
			for dh,dr,dc in zip(dz,drow,dcol):
				if 0 <= h+dh < z and 0 <= dr+row < y and 0 <= dc+col < x:
					if board[h+dh][dr+row][dc+col] == 0:
						next_q.append([h+dh,dr+row,dc+col])
						board[h+dh][dr+row][dc+col] = 1
						cnt -= 1
		answer += 1
		q = next_q
	if cnt == 0:
		return answer-1
	else:
		return -1

if __name__ == "__main__":
	x,y,z = map(int,input().split())
	board = []
	for _ in range(z):
		floor = []
		for _ in range(y):
			floor.append(list(map(int,input().split())))
		board.append(floor)
	print(solution(board,x,y,z))