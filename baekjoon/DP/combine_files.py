import sys
input = sys.stdin.readline

def solution(N,files):
	dp = [[99999999]*N for _ in range(N)]
	s = [[0]*N for _ in range(N)]
	for i in range(N):
		dp[i][i] = 0
		s[i][i] = files[i]
	
	for depth in range(1,N):
		for i in range(N-depth):
			for j in range(depth):
				s[i][depth+i] = s[i][i+j]+s[i+j+1][depth+i]
				dp[i][depth+i] = min(dp[i][depth+i],dp[i][i+j]+dp[i+j+1][depth+i]+s[i][depth+i])
		depth += 1 

	return dp[0][-1]

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		N = int(input())
		files = list(map(int,input().split()))
		print(solution(N,files))