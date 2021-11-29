import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	num = list(map(int,input().split()))
	dp = [[0]*N for _ in range(N)]
	for i in range(N):
		dp[i][i] = 1
		if i+1 < N:
			if num[i] == num[i+1]:
				dp[i][i+1] = 1
	for g in range(2,N):
		for r in range(N-g):
			if num[r] == num[r+g] and dp[r+1][r+g-1] == 1:
				dp[r][r+g] = 1

	T = int(input())
	for _ in range(T):
		S,E = map(int,input().split())
		print(dp[S-1][E-1])