import sys
from collections import deque
input = sys.stdin.readline

def move_white(board_q,row,col,i,way,units):
	d = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
	temp = deque()
	while board_q[row+d[way][0]][col+d[way][1]]:
		temp.append(board_q[row+d[way][0]][col+d[way][1]].popleft())

	board_q[row+d[way][0]][col+d[way][1]].append(board_q[row][col].popleft())
	while board_q[row+d[way][0]][col+d[way][1]][-1] != i:
		board_q[row+d[way][0]][col+d[way][1]].append(board_q[row][col].popleft())

	board_q[row+d[way][0]][col+d[way][1]] += temp

	for i in board_q[row+d[way][0]][col+d[way][1]]:
		units[i][0] = row+d[way][0]
		units[i][1] = col+d[way][1]


def solution(N,K,board,units):
	board_q = [[deque() for _ in range(N+2)] for _ in range(N+2)]
	d = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

	for i in range(K):
		row,col,way = units[i]
		board_q[row][col].append(i)
	cnt = 0
	while cnt < 1000:
		cnt+=1
		for i in range(K):
			row,col,way = units[i]
			if len(board_q[row][col]) >= 4:
				return cnt
			# 1 : right, 2 : left, 3 : up, 4 : down
			if board[row+d[way][0]][col+d[way][1]] == 0:
				move_white(board_q,row,col,i,way,units)
			elif board[row+d[way][0]][col+d[way][1]] == 1:
				move_white(board_q,row,col,i,way,units)
				row,col,way = units[i]
				temp = deque()
				while board_q[row][col][0] != i:
					temp.append(board_q[row][col].popleft())
				temp.append(board_q[row][col].popleft())
				temp = deque(reversed(temp))
				while board_q[row][col]:
					temp.append(board_q[row][col].pop())
				board_q[row][col] = temp
			else:
				for unit in board_q[row][col]:
					if units[unit][2] % 2 == 0:
						units[unit][2] -= 1
					else:
						units[unit][2] += 1
					if unit == i:
						break
				row,col,way = units[i]
				if board[row+d[way][0]][col+d[way][1]] == 0:
					move_white(board_q,row,col,i,way,units)
				elif board[row+d[way][0]][col+d[way][1]] == 1:
					move_white(board_q,row,col,i,way,units)
					row,col,way = units[i]
					temp = deque()
					while board_q[row][col][0] != i:
						temp.append(board_q[row][col].popleft())
					temp.append(board_q[row][col].popleft())
					temp = deque(reversed(temp))
					while board_q[row][col]:
						temp.append(board_q[row][col].pop())
					board_q[row][col] = temp
		if len(board_q[units[-1][0]][units[-1][1]]) >= 4:
			return cnt 
		for k in board_q[1:N+1]:
			print(k[1:N+1])
		for k in range(K):
			print(k,units[k])
		print()
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