import sys

input = sys.stdin.readline

def print_board(board):
	for row in range(9):
		for col in range(9):
			print(board[row][col],end=" ")
		print()

def search(board,blank,R,C,S,result):
	if len(blank) == 0:
		result[0] = 1
	else:
		if result[0] == 1:
			return
		else:
			row,col = blank[0]
			for i in range(1,10):
				if R[row][i-1] == 1:
					continue
				if C[col][i-1] == 1:
					continue
				if S[3*(row//3)+(i-1)//3][3*(col//3)+(i-1)%3] == 1:
					continue
				board[row][col] = i
				R[row][i-1] = 1
				C[col][i-1] = 1
				S[3*(row//3)+(i-1)//3][3*(col//3)+(i-1)%3] = 1
				search(board,blank[1:],R,C,S,result)
				if result[0] == 1:
					return
				else:
					board[row][col] = 0
					R[row][i-1] = 0
					C[col][i-1] = 0
					S[3*(row//3)+(i-1)//3][3*(col//3)+(i-1)%3] = 0


if __name__ == "__main__":
	board = []
	blank = []
	result = [0]
	R,C,S = [[0]*9 for _ in range(9)],[[0]*9 for _ in range(9)],[[0]*9 for _ in range(9)]
	for row in range(9):
		line = list(map(int,input().split()))
		for col in range(9):
			if line[col] != 0:
				R[row][line[col]-1] += 1
				C[col][line[col]-1] += 1
				S[(line[col]-1)//3 + 3*(row//3)][3*(col//3)+(line[col]-1)%3] += 1
			else:
				blank.append([row,col])
		board.append(line)
	search(board,blank,R,C,S,result)
	print()
	print_board(board)