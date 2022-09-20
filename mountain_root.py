import heapq

point = 0

def search(n,start,tree):
	q = []
	result = [0,1e9]
	visited = [0] * (n+1)
	heapq.heappush(q,[0,start])
	while q:
		cost,now = heapq.heappop(q)
		visited[now] = 1
		for path in tree[now]:
			end,time = path
			if visited[end] == 0 and point[end] == 0:
				heapq.heappush(q,[max(cost,time),end])
			elif visited[end] == 0 and point[end] == -1:
				if result[1] > max(cost,time):
					result = [end,max(cost,time)]
				elif result[1] == max(cost,time) and result[0] > end:
					result[0] = end
	return result


def solution(n,paths,gates,summits):
	global point
	point = [0] * (n+1)
	for i in gates:
		point[i] = 1
	for i in summits:
		point[i] = -1

	tree = dict()
	for i in range(n):
		tree[i+1] = []
	for path in paths:
		start,end,time = path
		tree[start].append([end,time])
		tree[end].append([start,time])

	answer = [0,1e9]
	for i in gates:
		result = search(n,i,tree)
		if answer[1] > result[1]:
			answer = result
		elif answer[1] == result[1] and answer[0] > result[0]:
			answer[0] = result[0]

	return answer

if __name__ == "__main__":
	print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2,3,4]))