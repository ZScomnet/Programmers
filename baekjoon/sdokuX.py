import sys

input = sys.stdin.readline

def print_board(board):
	for row in board:
		for col in row:
			print(col,end=" ")
		print()

def check_row(board,row):
	cnt = [0,0,0,0,0,0,0,0,0]
	for i in board[row]:
		if i == 0:
			continue
		if cnt[i-1] == 1:
			return False
		cnt[i-1] = 1

	return True

def check_col(board,col):
	cnt = [0,0,0,0,0,0,0,0,0]
	for i in range(9):
		if board[i][col] == 0:
			continue
		if cnt[board[i][col]-1] == 1:
			return False
		cnt[board[i][col]-1] = 1
	return True

def check_square(board,row,col):
	cnt = [0,0,0,0,0,0,0,0,0]
	for i in range(3):
		for j in range(3):
			if board[3*row+i][3*col+j] == 0:
				continue
			if cnt[board[3*row+i][3*col+j]-1] == 1:
				return False
			cnt[board[3*row+i][3*col+j]-1] = 1

	return True

def search(blank,num,board,check):
	print_board(board)
	if len(blank) == 0:
		check[0] = 1
		return
	for i in range(len(blank)):
		row,col = blank[i]
		for n in range(len(num)):
			board[row][col] = num[n]
			if check_row(board,row) and check_col(board,col) and check_square(board,row//3,col//3):
				search(blank[:i]+blank[i+1:],num[:n]+num[n+1:],board,check)
			if check[0] == 1:
				return
			else:
				board[row][col] = 0

def solution(blank,num,board):
	check = [0]
	search(blank,num,board,check)
	return board

if __name__ == "__main__":
	board = []
	blank = []
	num = []
	for n in range(9):
		cnt = [0,0,0,0,0,0,0,0,0]
		line = list(map(int,input().split()))
		for i in line:
			if i != 0:
				cnt[i-1] += 1
		for i in range(len(cnt)):
			if cnt[i] == 0:
				num.append(i+1)
			if line[i] == 0:
				blank.append([n,i])
		board.append(line)
	solution(blank,num,board)
	print_board(board)