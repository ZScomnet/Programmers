import sys
input = sys.stdin.readline

def solution():
	N = int(input())
	kids = []
	for _ in range(N):
		kids.append(int(input()))
	lis = 0
	dp = [1]*N
	for i in range(N):
		for j in range(i+1,N):
			if kids[i] < kids[j]:
				dp[j] = max(dp[i]+1,dp[j])
	return N-max(dp)

if __name__ == "__main__":
	print(solution())