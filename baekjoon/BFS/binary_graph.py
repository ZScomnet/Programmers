import sys
from collections import deque
input = sys.stdin.readline

def solution(V,E):
	edge = dict()
	graph = [0] * (V+1)

	for i in range(1,V+1):
		edge[i] = []
	for _ in range(E):
		start,end = map(int,input().split())
		edge[start].append(end)
		edge[end].append(start)

	for vertex in range(1,V+1):
		if graph[vertex] == 0:
			q = deque([vertex,])
			color = 1
			while q:
				next_q = deque()
				while q:
					now = q.popleft()
					graph[now] = color
					for i in edge[now]:
						if graph[i] == 0:
							next_q.append(i)
						elif graph[i] == color:
							return "NO"
				color *= -1
				q = next_q
	return "YES"

if __name__ == "__main__":
	K = int(input())
	for _ in range(K):
		V,E = map(int,input().split())
		print(solution(V,E))