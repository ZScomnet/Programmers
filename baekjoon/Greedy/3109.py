import sys
input = sys.stdin.readline

answer = [0]
flag = [0]
def dfs(board,row,col,R,C):
	if col == C-1:
		answer[0] += 1
		flag[0] = 1

	for dr in [-1,0,1]:
		if 0 <= row+dr < R and 0 <= col+1 < C:
			if board[row+dr][col+1] == '.':
				board[row+dr][col+1] = 'x'
				dfs(board,row+dr,col+1,R,C)
			if flag[0] == 1:
				return
def solution():
	R,C = map(int,input().split())
	board = []
	for _ in range(R):
		board.append(list(input()[:-1]))
	for row in range(R):
		flag[0] = 0
		dfs(board,row,0,R,C)
	return answer[0]

if __name__ == "__main__":
	print(solution())