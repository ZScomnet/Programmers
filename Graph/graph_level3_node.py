def solution(n,edge):
	graph = [[] for _ in range(n)]
	memory = [0 for _ in range(n)]
	memory[0] = -1
	for i in edge:
		graph[i[0]-1].append(i[1])
		graph[i[1]-1].append(i[0])
	start = [1]
	while True:
		next_start = []
		for num in start:
			for i in graph[num-1]:
				if memory[i-1] == 0:
					memory[i-1] = -1
					next_start.append(i)
		if len(next_start) == 0:
			break
		else:
			start = next_start
	return len(start)

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))