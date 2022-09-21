import heapq

def solution(n,paths,gates,summits):
	visited = [1e9] * (n+1)
	tree = dict()
	for i in range(n):
		tree[i+1] = []

	for path in paths:
		start,end,time = path
		tree[start].append([end,time])
		tree[end].append([start,time])

	for summit in summits:
		tree[summit] = 0

	q = []
	for i in gates:
		heapq.heappush(q,[0,i])

	answer = [1e9,1e9]
	while q:
		cost,now = heapq.heappop(q)
		if cost > answer[1]:
			break
		visited[now] = cost
		if tree[now] == 0:
			if answer[1] > cost:
				answer = [now,cost]
			elif answer[1] == cost:
				answer[0] = min(answer[0],now)
		else:
			for path in tree[now]:
				end,time = path
				if visited[end] > max(time,cost):
					visited[end] = max(time,cost)
					heapq.heappush(q,[max(time,cost),end])
	return answer

if __name__ == "__main__":
	print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2,3,4]))