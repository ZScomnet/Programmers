def solution(n,s,a,b,fares):
	graph = [[999999990] * n for _ in range(n)]
	answer = 999999990
	for i in range(n):
		graph[i][i] = 0

	for fare in fares:
		graph[fare[0]-1][fare[1]-1] = fare[2]
		graph[fare[1]-1][fare[0]-1] = fare[2]

	for mid in range(n):
		for start in range(n):
			for end in range(start,n):
				if start != end:
					cost = min(graph[start][end],graph[start][mid] + graph[mid][end])
					graph[start][end] = cost
					graph[end][start] = cost
	# 거쳐가는 곳 중 더 싼 곳이 있는가?
	for mid in range(n):
		cost = graph[s-1][mid] + graph[mid][a-1] + graph[mid][b-1]
		answer = min(answer,cost)

	return answer
print(solution(6,4,6,2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))