import sys
from collections import deque
input = sys.stdin.readline

def solution(V,E,pivot,graph):
	cost = [1e9] * (V+1)
	q = deque([pivot])
	cost[pivot] = 0
	while q: 
		for t in graph[q.popleft()]:
			start,end,value = t
			if cost[end] > cost[start] + value:
				cost[end] = cost[start] + value
				q.append(end)
	for i in range(1,len(cost)):
		if cost[i] == 1e9:
			print("INF")
		else:
			print(cost[i])

if __name__ == "__main__":
	V,E = map(int,input().split())
	pivot = int(input())
	graph = [[] for _ in range(V+1)]
	for _ in range(E):
		start,end,value = map(int,input().split())
		graph[start].append((start,end,value))
	solution(V,E,pivot,graph)