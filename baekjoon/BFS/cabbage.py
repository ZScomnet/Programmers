import sys
from collections import deque

input = sys.stdin.readline

def bfs(field,row,col):
	q = deque()
	q.append([row,col])
	while q:
		r,c = q.popleft()
		field[r][c] = 0
		if 0 <= r-1 < len(field):
			if field[r-1][c] == 1:
				q.append([r-1,c])
				field[r-1][c] = 0
		if 0 <= c+1 < len(field[r]):
			if field[r][c+1] == 1:
				q.append([r,c+1])
				field[r][c+1] = 0
		if 0 <= r+1 < len(field):
			if field[r+1][c] == 1:
				q.append([r+1,c])
				field[r+1][c] = 0
		if 0 <= c-1 < len(field[r]):
			if field[r][c-1] == 1:
				q.append([r,c-1])
				field[r][c-1]

def solution(field):
	answer = 0
	for row in range(len(field)):
		for col in range(len(field[row])):
			if field[row][col] == 1:
				bfs(field,row,col)
				answer += 1
	return answer

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		x,y,cabbage = map(int,input().split())
		field = [[0]*x for _ in range(y)]
		for _ in range(cabbage):
			col,row = map(int,input().split())
			field[row][col] = 1
		print(solution(field))
