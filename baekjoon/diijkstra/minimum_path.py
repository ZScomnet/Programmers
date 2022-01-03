import sys
from collections import deque
import heapq
input = sys.stdin.readline

def solution(V,E,start,edges):
	graph = dict()
	for i in range(V):
		graph[i+1] = []
	for edge in edges:
		s,e,v = edge
		graph[s].append((v,e))

	length = [1e9] * (V+1)
	q = []
	length[start] = 0
	heapq.heappush(q,(0,start))
	while q:
		value,now = heapq.heappop(q)
		if length[now] < value:
			continue
		for edge in graph[now]:
			total = value + edge[0]
			if total < length[edge[1]]:
				length[edge[1]] = total
				heapq.heappush(q,(total,edge[1]))

	for i in range(1,V+1):
		if length[i] == 1e9:
			print("INF")
		else:
			print(length[i])

if __name__ == "__main__":
	V,E = map(int,input().split())
	start = int(input())
	edges = []
	for _ in range(E):
		edges.append(list(map(int,input().split())))
	solution(V,E,start,edges)