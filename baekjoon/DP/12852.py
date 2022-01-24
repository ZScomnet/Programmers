import sys

input = sys.stdin.readline

import heapq
def solution(N):
	q = []
	count = [1e9] * (N+1)
	count[N] = 0
	heapq.heappush(q,(0,N))
	
	while q:
		cnt,now = heapq.heappop(q)
		if now == 1:
			break
		if count[now] < cnt:
			continue
		if now % 3 == 0 and count[now//3] > cnt:
			heapq.heappush(q,(cnt+1,now//3))
			count[now//3] = cnt+1
		if now % 2 == 0 and count[now//2] > cnt:
			heapq.heappush(q,(cnt+1,now//2))
			count[now//2] = cnt+1
		if now > 1 and count[now-1] == 1e9:
			heapq.heappush(q,(cnt+1,now-1))
			count[now-1] = cnt+1
	stack = [1]
	while stack[-1] != N:
		now = stack[-1]
		if now*3 <= N and now == stack[-1]:
			if count[now*3] == count[now]-1:
				stack.append(now*3)
		if now*2 <= N and now == stack[-1]:
			if count[now*2] == count[now]-1:
				stack.append(now*2)
		if count[now+1] == count[now]-1 and now == stack[-1]:
			stack.append(now+1)
		before = now
		if before == stack[-1]:
			count[before] = 1e9
			stack.pop()
		else:
			before = now
		
	print(len(stack)-1)
	for i in range(len(stack)):
		print(stack[-i-1],end=" ")
# from collections import deque
# def solution(N):
# 	dp = [1e9] * (N+1)
# 	dp[1] = 1
# 	q = deque([1])
# 	if N == 1:
# 		print(0)
# 		print(1)
# 		return
# 	cnt = 0
# 	while q:
# 		cnt += 1
# 		next_q = deque()
# 		print(q)
# 		while q:
# 			now = q.popleft()
# 			if dp[N] != 1e9:
# 				break
# 			if now*3 <= N and dp[now*3] == 1e9:
# 				dp[now*3] = cnt
# 				next_q.append(now*3)
# 			if now*2 <= N and dp[now*2] == 1e9:
# 				dp[now*2] = cnt
# 				next_q.append(now*2)
# 			if now+1 <= N and dp[now+1] == 1e9:
# 				dp[now+1] = cnt
# 				next_q.append(now+1)
# 		if dp[N] != 1e9:
# 			break
# 		else:
# 			q = next_q
# 	stack = [N]
# 	while stack[-1] != 1:
# 		if dp[stack[-1]//3] == dp[stack[-1]]-1:
# 			stack.append(N//3)
# 		elif dp[stack[-1]//2] == dp[stack[-1]]-1:
# 			stack.append(N//2)
# 		else:
# 			stack.append(N-1)
# 	print(len(stack)-1)
# 	for i in stack:
# 		print(i,end=" ")



if __name__ == "__main__":
	N = int(input())
	solution(N)