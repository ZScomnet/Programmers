import sys
from collections import deque
input = sys.stdin.readline

def solution(size):
	board = [[0]*size for _ in range(size)]
	drow,dcol = [-2,-1,1,2,2,1,-1,-2],[1,2,2,1,-1,-2,-2,-1]
	start = list(map(int,input().split()))
	end_row,end_col = map(int,input().split())
	answer = 0
	q = deque([start])
	while q:
		next_q = deque()
		while q:
			row,col = q.popleft()
			if row == end_row and col == end_col:
				return answer
			for dr,dc in zip(drow,dcol):
				if 0 <= dr+row < size and 0 <= dc+col < size:
					if board[dr+row][dc+col] == 0:
						next_q.append([dr+row,dc+col])
						board[dr+row][dc+col] = 1
		answer += 1
		q = next_q

if __name__ == "__main__":
	N = int(input())
	for _ in range(N):
		size = int(input())
		print(solution(size))
