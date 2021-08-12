def solution(n,k,cmd):
	row = [i for i in range(n)]
	memory = []
	for order in cmd:
		if order[0] == 'D':
			order = order.split()
			k += int(order[1])
		elif order[0] == 'U':
			order = order.split()
			k -= int(order[1])

		else:
			if order[0] == 'Z':
				row = row[:memory[-1]] + [memory[-1]] + row[memory[-1]:]
				if memory[-1] < k:
					k+=1
				memory.pop()
			else:
				memory.append(row[k])
				row = row[:k] + row[k+1:]
				if k == len(row):
					k -= 1
				
	result = ""
	if len(row) == 0:
		return "X"*n
	else:
		pivot = 0
		for r in row:
			result += "X"*(r-pivot) + "O"
			pivot = r+1
		result += "X"*(n-pivot)


	return result

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]Z))