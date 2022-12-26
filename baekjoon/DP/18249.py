import sys
input = sys.stdin.readline

def solution():
	T = int(input())
	dp = [1,2]
	for i in range(191229):
		dp.append((dp[-1]+dp[-2])%(10**9+7))
	for _ in range(T):
		N = int(input())
		print(dp[N-1])

if __name__ == "__main__":
	solution()