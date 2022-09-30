def solution():
	n,k = map(int,input().split())
	coins = []
	dp = [1e9] * (k+1)
	for _ in range(n):
		coins.append(int(input()))
		if coins[-1] <= k:
			dp[coins[-1]] = 1

	for i in range(1,k+1):
		if dp[i] == 1e9:
			continue
		for coin in coins:
			if i+coin <= k:
				dp[i+coin] = min(dp[i+coin],dp[i]+1)

	if dp[k] == 1e9:
		print(-1)
	else:
		print(dp[k])
if __name__ == "__main__":
	solution()