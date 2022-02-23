import sys
from collections import deque
input = sys.stdin.readline


def move(q,d,k):
	if d == 0:
		for _ in range(k):
			q.appendleft(q.pop())
	else:
		for _ in range(k):
			q.append(q.popleft())

def check(board,N,M):
	dx,dy = [-1,0,1,0],[0,1,0,-1]
	del_point = []
	num_point = []
	cnt = 0
	total = 0
	for row in range(N):
		for col in range(M):
			if board[row][col] > 0:
				cnt += 1
				total += board[row][col]
				num_point.append([row,col])
				for drow,dcol in zip(dx,dy):
					if 0 <= row+drow < N and -1 <= col+dcol < M:
						if board[row][col] == board[row+drow][col+dcol] != 0:
							del_point.append([row,col])
							break
					elif 0 <= row+drow < N and col+dcol == M:
						if board[row][col] == board[row+drow][0] != 0:
							del_point.append([row,col])
							break
	if del_point:
		for i in del_point:
			row,col = i
			board[row][col] = 0
	else:
		for i in num_point:
			row,col = i
			if board[row][col] > total/cnt:
				board[row][col] -= 1
			elif board[row][col] < total/cnt:
				board[row][col] += 1

def solution(N,M,T,board,spin):
	answer = 0
	for i in spin:
		x,d,k = i
		for j in range(x-1,len(board),x):
			move(board[j],d,k)
		check(board,N,M)

	for row in board:
		answer += sum(row)

	return answer

if __name__ == "__main__":
	N,M,T = map(int,input().split())
	board = []
	for _ in range(N):
		board.append(deque(list(map(int,input().split()))))
	spin = []
	for _ in range(T):
		spin.append(list(map(int,input().split())))
	print(solution(N,M,T,board,spin))