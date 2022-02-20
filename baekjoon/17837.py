import sys
from collections import deque
input = sys.stdin.readline

# 1 : right, 2 : left, 3 : up, 4 : down
way = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

def move(board_q,row,col,w,i):
	move_q = deque()
	move_q.append(board_q[row][col].popleft())

	while move_q[-1] != i:
		move_q.append(board_q[row][col].popleft())

	while move_q:
		board_q[row+w[0]][col+w[1]].appendleft(move_q.pop())	

def save(units,board_q,row,col):
	for i in board_q[row][col]:
		units[i-1][0] = row
		units[i-1][1] = col

def reverse(board_q,row,col,i):
	reverse_q = deque()
	reverse_q.append(board_q[row][col].popleft())

	while reverse_q[-1] != i:
		reverse_q.append(board_q[row][col].popleft())

	while reverse_q:
		board_q[row][col].append(reverse_q.pop())

def solution(N,K,board,units):
	board_q = [[deque() for _ in range(N+2)] for _ in range(N+2)] 
	for i in range(len(units)):
		row,col,w = units[i]
		board_q[row][col].append(i+1)
	cnt = 0
	while cnt <= 1000:
		cnt += 1
		# print(cnt)
		# for i in board_q:
		# 	print(i)
		# for i in units:
		# 	print(i)
		# print()
		for i in range(len(units)):
			row,col,w = units[i]
			if len(board_q[row][col]) >= 4:
				return cnt
			w = way[w]
			if board[row+w[0]][col+w[1]] == 0:
				move(board_q,row,col,w,i+1)
				save(units,board_q,row+w[0],col+w[1])
			elif board[row+w[0]][col+w[1]] == 1:
				move(board_q,row,col,w,i+1)
				reverse(board_q,row+w[0],col+w[1],i+1)
				save(units,board_q,row+w[0],col+w[1])
			else:
				if units[i][2] % 2 == 0:
					units[i][2] -= 1
				else:
					units[i][2] += 1
				row,col,w = units[i]
				w = way[w]
				if board[row+w[0]][col+w[1]] == 0:
					move(board_q,row,col,w,i+1)
					save(units,board_q,row+w[0],col+w[1])
				elif board[row+w[0]][col+w[1]] == 1:
					move(board_q,row,col,w,i+1)
					reverse(board_q,row+w[0],col+w[1],i+1)
					save(units,board_q,row+w[0],col+w[1])
			if len(board_q[units[i][0]][units[i][1]]) >= 4:
				return cnt 
	return -1

if __name__ == "__main__":
	N,K = map(int,input().split())
	board = [[2]*(N+2)]
	for _ in range(N):
		line = list(map(int,input().split()))
		board.append([2]+line+[2])
	board.append([2]*(N+2))
	units = []
	for i in range(K):
		units.append(list(map(int,input().split())))
	print(solution(N,K,board,units))