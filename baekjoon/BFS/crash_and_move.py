import sys
from collections import deque
input = sys.stdin.readline

def solution(board,R,C):
	q = deque()
	answer = 0
	q.append([0,0,-1])
	memory = [[1]*C for _ in range(R)]
	memory[0][0] = -1
	drow,dcol = [-1,0,1,0],[0,1,0,-1]
	if R == C == 1:
		return 1
	while q:
		next_q = deque()
		while q:
			row,col,now = q.popleft()
			for dr,dc in zip(drow,dcol):
				if 0 <= dr+row < R and 0 <= dc+col < C:
					if now == -1:
						if board[dr+row][dc+col] == '0' and (memory[dr+row][dc+col] == 1 or memory[dr+row][dc+col] == 0):
							memory[dr+row][dc+col] = -1
							next_q.append([dr+row,dc+col,-1])
						elif board[dr+row][dc+col] == '1' and memory[dr+row][dc+col] == 1:
							memory[dr+row][dc+col] = 0
							next_q.append([dr+row,dc+col,0])
					else:
						if board[dr+row][dc+col] == '0' and memory[dr+row][dc+col] == 1:
							memory[dr+row][dc+col] = 0
							next_q.append([dr+row,dc+col,0])
		answer += 1
		if memory[-1][-1] == 1:
			q = next_q
		else:
			break
	if memory[-1][-1] == 1:
		return -1
	else:
		return answer+1


if __name__ == "__main__":
	R,C = map(int,input().split())
	board = []
	for _ in range(R):
		board.append(list(input()[:-1]))
	print(solution(board,R,C))