import sys
from collections import deque

input = sys.stdin.readline

def solution(board):
	q = deque()
	cnt = 0
	answer = 0
	drow,dcol = [-1,0,1,0], [0,1,0,-1]

	for row in range(len(board)):
		for col in range(len(board[row])):
			if board[row][col] == 1:
				q.append([row,col])
			elif board[row][col] == 0:
				cnt += 1

	while q:
		next_q = deque()
		while q:
			row,col = q.popleft()
			for dr,dc in zip(drow,dcol):
				if 0 <= dr+row < len(board) and 0 <= dc+col < len(board[row]):
					if board[dr+row][dc+col] == 0:
						cnt -= 1
						next_q.append([dr+row,dc+col])
						board[dr+row][dc+col] = 1
		q = next_q
		answer += 1

	if cnt == 0:
		return answer-1
	else:
		return -1

if __name__ == "__main__":
	x,y = map(int,input().split())
	board = []
	for _ in range(y):
		board.append(list(map(int,input().split())))
	print(solution(board))	