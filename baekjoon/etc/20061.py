import sys
from collections import deque
input = sys.stdin.readline

board = [[0]*10 for _ in range(4)] + [[0]*4 for _ in range(6)]
for i in range(4):
	board[i].append(1)
board.append([1,1,1,1])

def check_blue():
	check = 0
	for i in range(2):
		check += max(board[0][4+i],board[1][4+i],board[2][4+i],board[3][4+i])
	for _ in range(check):
		for i in range(1,5):
			board[0][-1-i] = board[0][-1-i-1]
			board[1][-1-i] = board[1][-1-i-1]
			board[2][-1-i] = board[2][-1-i-1]
			board[3][-1-i] = board[3][-1-i-1]
	for i in range(4):
		board[i][4] = board[i][5] = 0

def check_green():
	check = 0
	for i in range(2):
		check += max(board[4+i][0],board[4+i][1],board[4+i][2],board[4+i][3])
	for _ in range(check):
		for i in range(1,5):
			board[-1-i][0] = board[-1-i-1][0]
			board[-1-i][1] = board[-1-i-1][1]
			board[-1-i][2] = board[-1-i-1][2]
			board[-1-i][3] = board[-1-i-1][3]
	for i in range(2):
		board[4+i][0] = board[4+i][1] = board[4+i][2] = board[4+i][3] = 0

def score_blue(answer):
	cols = deque()
	for i in range(4):
		if board[0][6+i] + board[1][6+i] + board[2][6+i] + board[3][6+i] == 4:
			cols.append(6+i)
	while cols:
		col = cols.popleft()
		answer[0] += 1
		for i in range(5):
			board[0][col-i] = board[0][col-1-i]
			board[1][col-i] = board[1][col-1-i] 
			board[2][col-i] = board[2][col-1-i]
			board[3][col-i] = board[3][col-1-i]

def score_green(answer):
	rows = deque()
	for i in range(4):
		if board[6+i][0] + board[6+i][1] + board[6+i][2] + board[6+i][3] == 4:
			rows.append(6+i)
	while rows:
		row = rows.popleft()
		answer[0] += 1
		for i in range(5):
			board[row-i][0] = board[row-1-i][0]
			board[row-i][1] = board[row-1-i][1]
			board[row-i][2] = board[row-1-i][2]
			board[row-i][3] = board[row-1-i][3]

def move_blue(t,row,col):
	check = deque()
	if t == 1:
		check.append([row,col])
	elif t == 2:
		check.append([row,col+1])
	else:
		check.append([row,col])
		check.append([row+1,col])

	while check:
		next_check = deque()
		while check:
			r,c = check.popleft()
			if board[r][c+1] == 0:
				next_check.append([r,c+1])
			else:
				if t == 1:
					board[r][c] = 1
				elif t == 2:
					board[r][c] = 1
					board[r][c-1] = 1
				else:
					board[r][c] = 1
					if r == row:
						board[r+1][c] = 1
					else:
						board[r-1][c] = 1
				next_check = []
				break
		check = next_check

def move_green(t,row,col):
	check = deque()
	if t == 1:
		check.append([row,col])
	elif t == 2:
		check.append([row,col])
		check.append([row,col+1])
	else:
		check.append([row+1,col])

	while check:
		next_check = deque()
		while check:
			r,c = check.popleft()
			if board[r+1][c] == 0:
				next_check.append([r+1,c])
			else:
				if t == 1:
					board[r][c] = 1
				elif t == 2:
					board[r][c] = 1
					if c == col:
						board[r][c+1] = 1
					else:
						board[r][c-1] = 1
				else:
					board[r-1][c] = 1
					board[r][c] = 1
				next_check = []
				break
		check = next_check

def solution(N,block):
	answer = [0]
	for b in block:
		t,row,col = b
		move_green(t,row,col)
		move_blue(t,row,col)
		score_green(answer)
		score_blue(answer)
		check_green()
		check_blue()
	print(answer[0])
	cnt = 0
	for row in range(4):
		for col in range(6,10):
			if board[row][col] == 1:
				cnt += 1
	for row in range(6,10):
		for col in range(4):
			if board[row][col] == 1:
				cnt += 1
	print(cnt)


if __name__ == "__main__":
	N = int(input())
	block = []
	for _ in range(N):
		block.append(list(map(int,input().split())))
	solution(N,block)