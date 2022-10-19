import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	box = list(map(int,input().split()))
	dp = [1]*n
	answer = 1
	for i in range(n):
		answer = max(answer,dp[i])
		for j in range(i+1,n):
			if box[i] < box[j]:
				dp[j] = max(dp[i]+1,dp[j])
	return answer

if __name__ == "__main__":
	print(solution())