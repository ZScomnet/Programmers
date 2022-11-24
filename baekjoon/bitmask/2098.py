import sys
input = sys.stdin.readline

# answer = [1e9]
# dp = [[0] * (1 << 16) for _ in range(16)]
# cost = []
# def dfs(visited,now,N,depth,end):
# 	if visited | 1 << 0 == end:
# 		answer[0] = min(dp[depth-1][visited]+cost[now][0],answer[0])
# 	else:
# 		for i in range(1,N):
# 			if visited & 1 << i == 0:
# 				dp[depth][visited | 1 << i] = dp[depth-1][visited] + cost[now][i]
# 				dfs(visited | 1 << i,i,N,depth+1,end)
# 				dp[depth][visited | 1 << i] = 1e9

# def solution():
# 	N = int(input())
# 	for row in range(N):
# 		cost.append(list(map(int,input().split())))
# 		for col in range(N):
# 			if row == col:
# 				continue
# 	for i in range(1,N):
# 		dp[0][1 << i] = cost[0][i]
# 	dfs(0, 0, N, 0, (1 << N)-1)
# 	return answer[0]
N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (1 << (N-1)) for _ in range(N)]
def tsp(now,visited):
	if dp[now][visited] != 0:
		return dp[now][visited]

	if visited == (1 << (N-1)) - 1:
		if cost[now][0] == 0:
			return 1e9
		else:
			return cost[now][0]

	minCost = 1e9

	for i in range(1,N):
		if visited & (1 << i-1):
			continue
		if cost[now][i] == 0:
			continue
		c = cost[now][i] + tsp(i,visited | 1 << (i-1))
		minCost = min(minCost, c)

	dp[now][visited] = minCost
	return minCost
def solution():
	return tsp(0,0)

if __name__ == "__main__":
	print(solution())