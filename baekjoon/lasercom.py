import sys
from collections import deque

input = sys.stdin.readline

def solution(w,h,board,start):
	q = deque([start,])
	board[start[0]][start[1]] = 0
	answer = 0
	drow,dcol = [-1,0,1,0],[0,1,0,-1]
	while q and answer == 0:
		count = 0
		way = [0,0,0,0]
		length = 1
		r,c = q.popleft()
		if [r,c] == start:
			count = 0
		else:
			count = board[r][c] + 1
		while way[0]+way[1]+way[2]+way[3] < 4 and answer == 0:
			for row,col,i in zip(drow,dcol,range(4)):
				if way[i] == 1:
					continue
				if 0 <= r+row*length < h and 0 <= c+col*length < w:
					if board[r+row*length][c+col*length] == '.':
						q.append([r+row*length,c+col*length])
						board[r+row*length][c+col*length] = count
					elif board[r+row*length][c+col*length] == '*':
						way[i] = 1
					elif board[r+row*length][c+col*length] == 'C':
						answer = count
						break
				else:
					way[i] = 1
			length += 1

	return answer

if __name__ == "__main__":
	w,h = map(int,input().split())
	board = []
	start = [-1,-1]
	for i in range(h):
		line = list(input())
		board.append(line[:-1])
		if start == [-1,-1]:
			for j in range(w):
				if line.pop() == 'C':
					start = [i,w-j]
					break
	print(solution(w,h,board,start))
