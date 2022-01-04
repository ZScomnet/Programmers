import sys
import heapq
input = sys.stdin.readline

def search(V,start,end,graph):
	answer = 0
	length = [1e9] * (V+1)
	length[start] = 0
	q = [(start,0)]
	while q:
		now,value = heapq.heappop(q)
		if length[now] < value:
			continue

		for edge in graph[now]:
			e,v = edge
			if v+value < length[e]:
				heapq.heappush(q,(e,v+value))
				length[e] = v+value

	return length[end]

def solution(V,E,edges,must):
	graph = dict()
	for i in range(1,V+1):
		graph[i] = []
	for edge in edges:
		heapq.heappush(graph[edge[0]],(edge[1],edge[2]))
		heapq.heappush(graph[edge[1]],(edge[0],edge[2]))
	length_A = search(V,1,must[0],graph.copy()) + search(V,must[0],must[1],graph.copy()) + search(V,must[1],V,graph.copy())
	length_B = search(V,1,must[1],graph.copy()) + search(V,must[1],must[0],graph.copy()) + search(V,must[0],V,graph.copy())
	if length_A >= 1e9 and length_B >= 1e9:
		return -1
	else:
		return min(length_A,length_B)

if __name__ == "__main__":
	V,E = map(int,input().split())
	edges = []
	for _ in range(E):
		edges.append(tuple(map(int,input().split())))
	must = list(map(int,input().split()))
	print(solution(V,E,edges,must))