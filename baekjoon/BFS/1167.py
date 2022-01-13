import sys
from collections import deque
input = sys.stdin.readline

def solution(V,tree):
	answer = 0
	count = [0] * (V+1)
	count[1] = 1
	q = deque([[1,0]])
	start,start_cost = 0,0
	while q:
		now,total = q.popleft()
		for edge in tree[now]:
			end,cost = edge
			if count[end] == 0:
				q.append([end,cost+total])
				count[end] = 1
			else:
				if start_cost < total:
					start = now
					start_cost = total
	count = [0] * (V+1)
	count[start] = 1
	q = deque([[start,0]])
	while q:
		now,total = q.popleft()
		for edge in tree[now]:
			end,cost = edge
			if count[end] == 0:
				q.append([end,cost+total])
				count[end] = 1
			else:
				if answer < total:
					answer = total

	return answer

if __name__ == "__main__":
	V = int(input())
	tree = dict()
	for _ in range(V):
		line = list(map(int,input().split()))
		tree[line[0]] = []
		for i in range(1,len(line)-1,2):
			tree[line[0]].append([line[i],line[i+1]])
	print(solution(V,tree))