import sys
input = sys.stdin.readline

def search(cost,dp,N,start,visited):
	if visited == (1 << N)-1:
		if cost[start][0]:
			return cost[start][0]
		else:
			return 1e9
	if dp[start][visited] != 1e9:
		return dp[start][visited]

	for i in range(1,N):
		if cost[start][i] == 0 or visited & (1 << i):
			continue
		dp[start][visited] = min(dp[start][visited],search(cost,dp,N,i,visited | (1 << i))+cost[start][i])
	return dp[start][visited]

def solution():
	N = int(input())
	cost = []
	dp = [[1e9]*(1 << N) for _ in range(N)]
	for _ in range(N):
		cost.append(list(map(int,input().split())))
	answer = search(cost,dp,N,0,1)
	return answer

if __name__ == "__main__":
	print(solution())