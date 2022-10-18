import sys
input = sys.stdin.readline

# def solution():
# 	N,K = map(int,input().split())
# 	dp = [[0]*(N+1) for _ in range(K+1)]
# 	dp[1] = [1]*(N+1)
# 	for i in range(2,K+1):
# 		dp[i][0] = 1
# 		for j in range(1,N+1):
# 			for num in range(j+1):
# 				dp[i][j] += dp[i-1][j-num]
# 				dp[i][j] %= 1000000000

# 	return dp[-1][-1]

def solution():
	N, K = map(int,input().split())
	dp = [[0]*(N+1) for _ in range(K+1)]
	dp[1] = [1]*(N+1)
	if K >= 2:
		dp[2] = [2]*(N+1)
	for i in range(2,K+1):
		dp[i][1] = i
		for j in range(2,N+1):
			dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % 1000000000

	return dp[-1][-1]

if __name__ == "__main__":
	print(solution())