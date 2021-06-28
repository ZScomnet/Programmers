def solution(operations):
	queue = []
	for i in operations:
		if i[0] == 'I':
			queue.append( int(i[2:]) )
		elif "D -1" in i and len(queue) != 0:
			del queue[queue.index(min(queue))]
		elif "D 1" in i and len(queue) != 0:
			del queue[queue.index(max(queue))]

	if len(queue) == 0:
		return [0,0]
	else:
		return [max(queue),min(queue)]

print(solution(["I 7","I 5","I -5","D -1"]))