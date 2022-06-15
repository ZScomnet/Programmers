from collections import deque

d = [(-1,0),(0,1),(1,0),(0,-1)]

def solution(board):
	R,C = len(board),len(board[0])
	cost = [[10000]*C for _ in range(R)]
	cost[0][0] = 0
	q = deque()
	q.append([0,0])

	while q:
		row,col = q.popleft()
		if row == R-1 and col == C-1:
			continue
		cost[row][col] += 500
		if row == 0 and col == 0:
			cost[row][col] -= 500

		way = [0,0,0,0]
		for i in range(1,R):
			for j in range(4):
				drow,dcol = d[j][0]*i,d[j][1]*i
				if way[j] == 0 and 0 <= row+drow < R and 0 <= col+dcol < C:
					if board[row+drow][col+dcol] == 1:
						way[j] = 1
						continue
					if cost[row+drow][col+dcol] > cost[row][col]+100*i:
						q.append([row+drow,col+dcol])
						cost[row+drow][col+dcol] = cost[row][col]+100*i
				else:
					way[j] = 1
			if way[0] == way[1] == way[2] == way[3] == 1:
				break

	return cost[R-1][C-1]

if __name__ == "__main__":
	print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))