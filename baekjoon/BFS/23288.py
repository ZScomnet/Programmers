import sys
from collections import deque
input = sys.stdin.readline

board = []
check = []
dice = [1,2,3,4,5,6] # up back right left front down
way = [4] # 1 : back / 2 : front / 3 : left / 4 : right 
m = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
idx = [1,1]
answer = [0]

def spin_dice():
	global dice
	up,back,right,left,front,down = dice
	if way[0] == 1: # back
		dice = [front,up,right,left,down,back]
	elif way[0] == 2: # right
		dice = [back,down,right,left,up,front]
	elif way[0] == 3: # left
		dice = [right,back,down,up,front,left]
	else: # front
		dice = [left,back,up,down,front,right]

def move():
	global idx
	drow,dcol = m[way[0]]
	row,col = idx
	if board[row+drow][col+dcol] == -1:
		if way[0] % 2 == 0:
			way[0] -= 1
		else:
			way[0] += 1
		drow,dcol = m[way[0]]
	idx = [row+drow,col+dcol]
	spin_dice()

def bfs():
	q = deque([idx])
	reset = deque()
	value = board[idx[0]][idx[1]]
	while q:
		row,col = q.popleft()
		reset.append([row,col])
		check[row][col] = 1
		answer[0] += value
		for w in [(-1,0),(0,1),(1,0),(0,-1)]:
			drow,dcol = w
			if value == board[row+drow][col+dcol] and check[row+drow][col+dcol] == 0:
				q.append([row+drow,col+dcol])
				check[row+drow][col+dcol] = 1
	while reset:
		row,col = reset.popleft()
		check[row][col] = 0

def spin_way():
	A,B = dice[-1],board[idx[0]][idx[1]]
	if A > B:
		if way[0] == 1:
			way[0] = 4
		elif way[0] == 2:
			way[0] = 3
		elif way[0] == 3:
			way[0] = 1
		else:
			way[0] = 2
	elif A < B:
		if way[0] == 1:
			way[0] = 3
		elif way[0] == 2:
			way[0] = 4
		elif way[0] == 3:
			way[0] = 2
		else:
			way[0] = 1

def solution(N,M,K):
	for _ in range(K):
		move()
		bfs()
		spin_way()

	return answer[0]

if __name__ == "__main__":
	N,M,K = map(int,input().split())
	board.append([-1]*(M+2))
	check.append([0]*(M+2))
	for _ in range(N):
		board.append([-1] + list(map(int,input().split())) + [-1])
		check.append([0]*(M+2))
	board.append([-1]*(M+2))
	check.append([0]*(M+2))
	print(solution(N,M,K))