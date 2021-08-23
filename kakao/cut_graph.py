def solution(n,k,cmd):
	graph = [i for i in range(n)]
	result = ['X' for _ in range(n)]
	graph_stack = []
	index = k
	for c in cmd:
		if c[0] == 'U':
			index -= int(c[2])
		elif c[0] == 'D':
			index += int(c[2])
		elif c[0] == 'C':
			del_stack.append(graph)
			del graph[index]
			if index == len(graph):
				index -= 1
		else:
			graph = del_stack.pop()
	for i in graph:
		result[i] = 'O'
	answer = ""
	for i in result:
		answer += i
	return answer

if __name__ == "__main__":
	print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))