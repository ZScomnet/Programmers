import sys
sys.setrecursionlimit(300001)

counter = [0] * 300001
result = 0

def search(a,tree,before,now):
	counter[now] = 1
	global result
	for i in tree[now]:
		if counter[i] == 0:
			search(a,tree,now,i)
	if before != -1:
		a[before] += a[now]
		result += abs(a[now])

def solution(a,edges):
	tree = dict()
	for i in range(len(a)):
		tree[i] = []
	for edge in edges:
		start,end = edge
		tree[start].append(end)
		tree[end].append(start)
	search(a,tree,-1,0)
	if a[0] == 0:
		return result
	else:
		return -1

if __name__ == "__main__":
	print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))