import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(N,start,graph):
	q = []
	cost = [INF] * (N+1)
	cost[start] = 0
	heapq.heappush(q,[0,start])
	while q:
		c,now = heapq.heappop(q)
		if cost[now] < c:
			continue
		for edge in graph[now]:
			if cost[edge[0]] > c + edge[1]:
				cost[edge[0]] = c + edge[1]
				heapq.heappush(q,[edge[1]+c,edge[0]])
	return cost

def solution(N,start,end,graph):
	cost = dijkstra(N,start,graph)
	for i in sorted(end):
		if cost[i] != INF and cost[i] % 2 == 1:
			print(i,end=" ")
	print()

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		N,E,M = map(int,input().split())
		graph = [[] for _ in range(N+1)]
		start,m1,m2 = map(int,input().split())
		for _ in range(E):
			n1,n2,cost = map(int,input().split())
			if (n1 == m1 and n2 == m2) or (n1 == m2 and n2 == m1):
				graph[n1].append([n2,2*cost-1])
				graph[n2].append([n1,2*cost-1])
			else:
				graph[n1].append([n2,2*cost])
				graph[n2].append([n1,2*cost])
		end = []
		for _ in range(M):
			end.append(int(input()))
		solution(N,start,end,graph)