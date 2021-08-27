def solution(n,t,m,p):
	answer = ""
	stack = [0]
	dic = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
	loop = 0
	while len(stack) < m*t:
		index = loop
		cycle = []
		while index != 0:
			if index % n < 10:
				cycle.append(index%n)
			else:
				cycle.append(dic[index%n])
			index = index // n
		stack += reversed(cycle)
		loop += 1
	for i in range(t):
		answer += str(stack[m*i+p-1])

	return answer

if __name__ == "__main__":
	print(solution(2,4,2,1))