import sys
from collections import deque
input = sys.stdin.readline

def solution(maze):
	q = deque()
	q.append([0,0])
	maze[0][0] = 0
	answer = 1
	while True:
		next_q = deque()
		while q:
			row,col = q.popleft()
			if 0 <= row-1 < len(maze):
				if maze[row-1][col] == '1':
					maze[row-1][col] = '0'
					next_q.append([row-1,col])
			if 0 <= col+1 < len(maze[row]):
				if maze[row][col+1] == '1':
					maze[row][col+1] = '0'
					next_q.append([row,col+1])
			if 0 <= row+1 < len(maze):
				if maze[row+1][col] == '1':
					maze[row+1][col] = '0'
					next_q.append([row+1,col])
			if 0 <= col-1 < len(maze[row]):
				if maze[row][col-1] == '1':
					maze[row][col-1] = '0'
					next_q.append([row,col-1])
		answer += 1
		if maze[-1][-1] == '0':
			break
		q = next_q
	return answer

if __name__ == "__main__":
	row,col = map(int,input().split())
	maze = []
	for _ in range(row):
		maze.append(list(input())[:-1])
	print(solution(maze))