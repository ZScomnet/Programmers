import sys
from collections import deque
INF = float('inf')
input = sys.stdin.readline

def solution(N,K):
	field = [INF] * 100001
	field[N] = 0
	q = deque()
	q.append(N)
	while q:
		next_q = deque()
		while q:
			now = q.popleft()
			if now-1 >= 0 and field[now-1] == INF:
				q.append(now-1)
				field[now-1] = field[now]+1
			if now+1 < 100001 and field[now+1] == INF:
				q.append(now+1)
				field[now+1] = field[now]+1
			if now*2 < 100001:
				if field[now*2] == INF:
					q.append(now*2)
					field[now*2] = field[now]+1
		if field[K] != INF:
			break
	stack = [K]
	while stack[-1] != N:
		now = stack[-1]
		if now-1 >= 0:
			if field[now-1]+1 == field[now] and now == stack[-1]:
				stack.append(now-1)
		if now+1 < 100001:
			if field[now+1]+1 == field[now] and now == stack[-1]:
				stack.append(now+1)
		if field[now//2]+1 == field[now] and now % 2 == 0 and now == stack[-1]:
			stack.append(now//2)
		if now == stack[-1]:
			field[now] = -100
			stack.pop()
	print(field[K])
	while stack:
		print(stack.pop(),end=" ")

if __name__ == "__main__":
	N,K = map(int,input().split())
	solution(N,K)