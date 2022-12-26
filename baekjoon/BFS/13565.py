from collections import deque
import sys
input = sys.stdin.readline

def solution():
	R,C = map(int,input().split())
	board = []
	for _ in range(R):
		board.append(list(input().rstrip()))

	q = deque()
	for i in range(C):
		if board[0][i] == '0':
			board[0][i] = '1'
			q.append([0,i])

	while q:
		row,col = q.popleft()
		if row == R-1:
			return "YES"
		for drow,dcol in zip([-1,0,1,0],[0,1,0,-1]):
			if 0 <= row+drow < R and 0 <= col+dcol < C:
				if board[row+drow][col+dcol] == '0':
					q.append([row+drow,col+dcol])
					board[row+drow][col+dcol] = '1'

	return "NO"

if __name__ == "__main__":
	print(solution())