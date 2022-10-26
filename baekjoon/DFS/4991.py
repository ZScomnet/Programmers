import sys
from collections import deque
input = sys.stdin.readline

answer = [1e9]

def bfs(R,C,board,row,col,length,idx,cnt):
	visited = [[0]*C for _ in range(R)]
	q = deque()
	q.append([row,col])
	while q:
		r,c = q.popleft()
		for dr,dc in zip((-1,0,1,0),(0,1,0,-1)):
			if 0 <= r+dr < R and 0 <= c+dc < C:
				if board[r+dr][c+dc] == 'x' or visited[r+dr][c+dc] != 0:
					continue
				visited[r+dr][c+dc] = visited[r][c]+1
				q.append([r+dr,c+dc])
				if board[r+dr][c+dc] != '.' and idx != board[r+dr][c+dc]:
					length[idx][board[r+dr][c+dc]] = visited[r+dr][c+dc]
					cnt -= 1
	if cnt == 1:
		return True
	else:
		return False

def dfs(length,now,state,depth,cost):
	if depth == len(length):
		answer[0] = min(answer[0],cost)
		return
	for i in range(1,len(length)):
		if state[i] == 0:
			state[i] = 1
			dfs(length,i,state,depth+1,cost+length[now][i])
			state[i] = 0

def solution(R,C):
	board = []
	cnt = 1
	start = [[]]
	for r in range(R):
		line = list(input()[:-1])
		for c in range(C):
			if line[c] == '*':
				line[c] = cnt
				cnt += 1
				start.append([r,c])
			elif line[c] == 'o':
				start[0] = [r,c]
				line[c] = 0
		board.append(line)
	length = [[0]*cnt for _ in range(cnt)]
	for i in range(cnt):
		row,col = start[i]
		result = bfs(R,C,board,row,col,length,i,cnt)
	if result:
		state = [0]*cnt
		dfs(length,0,state,1,0)
		return answer[0]
	return -1

if __name__ == "__main__":
	while True:
		R,C = map(int,input().split())
		if R == C == 0:
			break
		print(solution(C,R))
		answer[0] = 1e9