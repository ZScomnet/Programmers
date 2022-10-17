import sys
input = sys.stdin.readline

def solution():
	N = int(input())
	board = []
	for _ in range(N):
		board.append(list(map(int,input().split())))
	dp = [[0]*N for _ in range(N)]
	dp[0][0] = 1
	for row in range(N):
		for col in range(N):
			if board[row][col] == 0:
				break
			if 0 <= col+board[row][col] < N:
				dp[row][col+board[row][col]] += dp[row][col]
			if 0 <= row+board[row][col] < N:
				dp[row+board[row][col]][col] += dp[row][col]

	return dp[-1][-1]

if __name__ == "__main__":
	print(solution())