import sys
input = sys.stdin.readline

def solution(n):
	dp = [[0]*2 for _ in range(n)]
	dp[0] = [1,2]
	for i in range(1,n):
		dp[i][0] = (dp[i-1][0]+dp[i-1][1]) % 9901
		dp[i][1] = (dp[i-1][0]+dp[i-1][1]//2) % 9901
		dp[i][1] *= 2

	return sum(dp[-1]) % 9901

if __name__ == "__main__":
	print(solution(int(input())))