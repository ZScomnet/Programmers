import sys
input = sys.stdin.readline

def solution():
	T = int(input())
	for _ in range(T):
		n = int(input())
		board = []
		board.append(list(map(int,input().split())))
		board.append(list(map(int,input().split())))
		dp = [[0]*n,[0]*n]
		dp[0][0] = board[0][0]
		dp[1][0] = board[1][0]
		for i in range(1,n):
			dp[0][i] = max(dp[0][i-1],dp[1][i-1]+board[0][i])
			dp[1][i] = max(dp[1][i-1],dp[0][i-1]+board[1][i])
		print(max(dp[0][-1],dp[1][-1]))

if __name__ == "__main__":
	solution()