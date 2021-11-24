import sys
input = sys.stdin.readline
sys.setrecursionlimit(25001)

drow,dcol = [-1,0,1,0],[0,1,0,-1]

def search(R,C,board,memory,row,col):
	if row == R-1 and col == C-1:
		memory[row][col] = 1
	else:
		if memory[row][col] == -1:
			memory[row][col] = 0
		for dr,dc in zip(drow,dcol):
			if 0 <= dr+row < R and 0 <= dc+col < C:
				if board[row][col] > board[dr+row][dc+col] and memory[dr+row][dc+col] == -1:
					search(R,C,board,memory,dr+row,dc+col)
		for dr,dc in zip(drow,dcol):
			if 0 <= dr+row < R and 0 <= dc+col < C:
				if board[row][col] > board[dr+row][dc+col] and memory[dr+row][dc+col] >= 0:
					memory[row][col] += memory[dr+row][dc+col]

def solution(R,C,board):
	memory = [[-1]*C for _ in range(R)]
	search(R,C,board,memory,0,0)
	return memory[0][0]

if __name__ == "__main__":
	R,C = map(int,input().split())
	board = []
	for _ in range(R):
		board.append(list(map(int,input().split())))
	print(solution(R,C,board))