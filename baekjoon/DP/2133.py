import sys
input = sys.stdin.readline

def solution(n):
	if n % 2 == 1:
		return 0
	else:
		dp = [0] * (n+1)
		dp[2] = 3
		for i in range(4,n+1,2):
			dp[i] = dp[i-2] * dp[2] + 2
			for j in range(4,i,2):
				dp[i] += dp[i-j] * 2
		return dp[n]

if __name__ == "__main__":
	print(solution(int(input())))
