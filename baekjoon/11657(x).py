import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = float('inf')

def solution(N,M,graph):
	cost = [INF] * (N+1)
	cost[1] = 0
	count = [0] * (N+1)
	count[1] = 1
	q = deque()
	q.append(1)
	while q:
		next_q = deque()
		while q:
			now = q.popleft()
			for edge in graph[now]:
				end,c = edge
				if cost[end] > cost[now] + c:
					cost[end] = cost[now] + c
					count[end] += 1
					next_q.append(end)
					if count[end] > N:
						print(-1)
						return
		q = next_q

	for i in cost[2:]:
		if i != INF:
			print(i)
		else:
			print(-1)

if __name__ == "__main__":
	N,M = map(int,input().split())
	graph = dict()
	for i in range(1,N+1):
		graph[i] = []
	# for _ in range(M):
	# 	A,B,C = map(int,input().split())
	# 	graph[A].append([B,C])
	for i in range(1,N):
		graph[i].append([i+1,-10000])
	graph[500].append([1,-10000])
	solution(N,M,graph)

# def solution(N,M,graph):
# 	cost = [[INF,i] for i in range(N+1)]
# 	count = [0] * (N+1)
# 	cost[1][0] = 0
# 	q = []
# 	heapq.heappush(q,[0,1])
# 	while q:
# 		time,now = heapq.heappop(q)
# 		if time > cost[now][0]:
# 			continue
# 		cost[now][0] = time
# 		count[now] += 1
# 		if count[now] > N:
# 			print(-1)
# 			return
# 		for bus in graph[now]:
# 			end,c = bus
# 			if cost[end][0] > time + c:
# 				heapq.heappush(q,[time+c,end]) 
# 	for i in cost[2:]:
# 		if i[0] != INF:
# 			print(i[0])
# 		else:
# 			print(-1)
