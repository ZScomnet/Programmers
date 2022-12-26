from heapq import heappush,heappop
import sys
input = sys.stdin.readline

def solution():
	N, M = map(int,input().split())
	nums = [int(input()) for _ in range(N)]
	dp = [[0]*(N) for _ in range(N)]
	q = []
	for row in range(N):
		dp[row][row] = nums[row]
		heappush(q,[-dp[row][row],row,row])
		for col in range(row+1,N):
			dp[row][col] = dp[row][col-1] + nums[col]
			heappush(q,[-dp[row][col],row,col])
	answer = 0
	while q:
		sums, start, end = heappop(q)
		sums *= -1
		if start == 0:
			if N-1-end >= M-1:
				answer = sums
				break
		elif end == N-1:
			if start >= M-1:
				answer = sums
				break
		else:
			if M-1 >= 2 and start+N-1-end >= M-1:
				answer = sums
				break
	return answer

if __name__ == "__main__":
	print(solution())