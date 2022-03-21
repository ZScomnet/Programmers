import sys
from collections import deque
input = sys.stdin.readline

board = []
customer = []
d = [(-1,0),(0,-1),(0,1),(1,0)]


def bfs_customer(taxi):
	q = deque([taxi+[0]])
	board_cnt = [[0]*len(board) for _ in range(len(board))]
	while q:
		row,col,cnt = q.popleft()
		if board[row][col] < 0:
			return [row,col,cnt]
		for i in d:
			dr,dc = i
			if board[row+dr][col+dc] == 0 and board_cnt[row+dr][col+dc] == 0:
				board_cnt[row+dr][col+dc] = cnt+1
				q.append([row+dr,col+dc,cnt+1])
			elif board[row+dr][col+dc] < 0:
				return [row+dr,col+dc,cnt+1]

def bfs_finish(customer):
	board_cnt = [[0]*len(board) for _ in range(len(board))]
	sr,sc,fr,fc = customer
	q = deque([[sr,sc,0]])
	while q:
		row,col,cnt = q.popleft()
		board_cnt[row][col] = cnt
		if row == fr and col == fc:
			return cnt
		for i in d:
			dr,dc = i
			if board[row+dr][col+dc] < 1 and board_cnt[row+dr][col+dc] == 0:
				board_cnt[row+dr][col+dc] = cnt+1
				q.append([row+dr,col+dc,cnt+1])

def solution(taxi,N,M,oil):
	cus = len(customer)
	cost = []
	for i in range(len(customer)):
		sr,sc,fr,fc = customer[i]
		if sr == sc == 0:
			continue
		board[sr][sc] = -1*(i+1)
		cost.append(bfs_finish(customer[i]))
		if cost[-1] == None:
			return -1

	while cus != 0:
		start = bfs_customer(taxi)
		row,col,l = start
		oil -= l
		if oil < 0:
			return -1
		idx = -1*board[row][col]-1
		if oil - cost[idx] < 0:
			return -1
		oil += cost[idx]
		if oil > 0:
			cus -= 1
		else:
			return -1
		taxi = [customer[idx][2],customer[idx][3]]
		board[customer[idx][0]][customer[idx][1]] = 0
		customer[idx] = [0,0,0,0]

	return oil

if __name__ == "__main__":
	N,M,oil = map(int,input().split())
	board.append([1]*(N+2))
	for _ in range(N):
		board.append([1]+list(map(int,input().split()))+[1])
	board.append([1]*(N+2))
	taxi = list(map(int,input().split()))
	for _ in range(M):
		customer.append(list(map(int,input().split())))
	print(solution(taxi,N,M,oil))