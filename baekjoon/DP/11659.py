import sys
input = sys.stdin.readline

def solution():
	N, M = map(int,input().split())
	num = list(map(int,input().split()))
	dp = [0] * (N+1)
	for i in range(1,N+1):
		dp[i] = dp[i-1] + num[i-1]
	for _ in range(M):
		start,end = map(int,input().split())
		print(dp[end]-dp[start-1])

if __name__ == "__main__":
	solution()