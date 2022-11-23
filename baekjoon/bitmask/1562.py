def solution(N):
	dp = [[[0]*(1 << 10) for _ in range(10)] for _ in range(N)]
	for i in range(1,10):
		dp[0][i][1 << i] = 1

	for i in range(1,N):
		for j in range(10):
			for k in range(1 << 10):
				if j == 0:
					dp[i][0][k | (1 << 0)] = (dp[i][0][k | (1 << 0)] + dp[i-1][1][k]) % 1000000000
				elif j == 9:
					dp[i][9][k | (1 << 9)] = (dp[i][9][k | (1 << 9)] + dp[i-1][8][k]) % 1000000000
				else:
					dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i-1][j-1][k]) % 1000000000
					dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i-1][j+1][k]) % 1000000000

	answer = 0
	for i in range(10):
		answer = (answer + dp[-1][i][-1]) % 1000000000
	return answer
if __name__ == "__main__":
	print(solution(int(input())))