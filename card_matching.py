from collections import deque

answer = [1e9]

def find(board,r,c,card):
	visited = [[1e9]*4 for _ in range(4)]
	visited[r][c] = 0
	q = deque()
	q.append([r,c])
	while q:
		row,col = q.popleft()
		for dr,dc in zip((-1,0,1,0),(0,1,0,-1)):
			if 0 <= row+dr < 4 and 0 <= col+dc < 4:
				if visited[row+dr][col+dc] > visited[row][col]+1:
					q.append([row+dr][col+dc])
					if board[r][c] == board[row+dr][col+dc]:
						return [visited[row][col]+1,row+dr,col+dc]
					visited[row+dr][col+dc] = visited[row][col]+1
			for ctrl in range(1,4):
				if 0 <= row+dr*ctrl < 4 and 0 <= col+dc*ctrl < 4:
					if board[row+dr*ctrl][col+dc*ctrl] == board[r][c]:
						return [visited[row][col]+1,row+dr*ctrl,col+dc*ctrl]
					elif board[row+dr*ctrl][col+dc*ctrl] != 0 and visited[row+dr*ctrl][col+dc*ctrl] > visited[row][col]+1:
						visited[row+dr*ctrl][col+dc*ctrl] = visited[row][col]+1
						q.append([row+dr*ctrl,col+dc*ctrl])
						break
				else:
					if visited[row+dr*(ctrl-1)][col+dc*(ctrl-1)] > visited[row][col]+1:
						visited[row+dr*(ctrl-1)][col+dc*(ctrl-1)] = visited[row][col]+1
						q.append([row+dr*(ctrl-1),col+dc*(ctrl-1)])
						break



def search(board,r,c,cnt):
	visited = [[0]*4 for _ in range(4)]
	cnt = 16
	q = deque()
	q.append([r,c])
	while q:
		row,col = q.popleft()
		visited[row][col] = 1
		if 

def solution(board,r,c):
	card_cnt = 0
	for i in range(4):
		for j in range(4):
			if board[i][j] != 0:
				card_cnt += 1
	card_cnt = card_cnt // 2
	search(board,r,c,card_cnt)

	return answer[0]

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))