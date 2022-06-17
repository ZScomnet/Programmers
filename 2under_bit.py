def solution(numbers):
	answer = []
	for num in numbers:
		n = []
		if num == 0:
			answer.append(1)
			continue
		while num >= 1:
			n.append(num%2)
			num = num // 2

		n.append(0)
		for i in range(len(n)-1):
			if i == 0 and n[i] == 0:
				n[0] = 1
				break
			elif n[i] == 1 and n[i+1] == 0:
				n[i] = 0
				n[i+1] = 1
				break
		result = 0
		for i in range(len(n)):
			result += (2**(i)) * n[i]
		answer.append(result)


	return answer

if __name__ == "__main__":
	print(solution([1]))