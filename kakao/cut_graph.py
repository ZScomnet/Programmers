def solution(n,k,cmd):
	link = {i : [i-1,i+1] for i in range(n)}
	result = ['O' for _ in range(n)]
	stack = []
	for c in cmd:
		if c[0] == 'U':
			for _ in range(int(c[2:])):
				k = link[k][0]
		elif c[0] == 'D':
			for _ in range(int(c[2:])):
				k = link[k][1]
		elif c[0] == 'C':
			stack.append([link[k][0],k,link[k][1]])
			result[k] = 'X'
			
			if link[k][1] != n:
				link[link[k][1]][0] = link[k][0]
			if link[k][0] != -1:
				link[link[k][0]][1] = link[k][1]
			if link[k][1] == n:
				k = link[k][0]
			else:
				k = link[k][1]
		else:
			back = stack.pop()
			if k == -1 or k == n:
				k = back[1]
			if back[0] != -1:
				link[back[0]][1] = back[1]
			if back[2] != n:
				link[back[2]][0] = back[1]
			link[back[1]][0] = back[0]
			link[back[1]][1] = back[2]
			result[back[1]] = 'O'

	answer = ""
	for i in result:
		answer += i

	return answer

if __name__ == "__main__":
	print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))