import sys
from collections import deque
input = sys.stdin.readline

def search(tree,start,N):
	q = deque([[start,0]])
	count = [0] * (N+1)
	count[start] = 1
	result = [0,0]
	while q:
		now,total = q.popleft()
		for edge in tree[now]:
			node,cost = edge
			if count[node] == 0:
				q.append([node,total+cost])
				count[node] = 1
		if result[1] < total:
			result = [now,total] 
	return result

def solution(tree,N):
	if N > 1:
		start = search(tree,1,N)
		answer = search(tree,start[0],N)
	else:
		return 0
	return answer[1]

if __name__ == "__main__":
	N = int(input())
	tree = dict()
	for i in range(1,N+1):
		tree[i] = []
	for _ in range(N-1):
		n1,n2,cost = map(int,input().split())
		tree[n1].append([n2,cost])
		tree[n2].append([n1,cost])

	print(solution(tree,N))