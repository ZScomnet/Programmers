def solution(number,k):
	result = []
	for i in number:
		if len(result) == 0 or k == 0:
			result.append(i)
		else:
			for j in range(len(result)-1,-1,-1):
				if result[j] < i and k != 0:
					del result[j]
					k -= 1
				else:
					break
			result.append(i)
	if len(result) != len(number) - k:
		for _ in range(k):
			del result[-1]

	return ''.join(result)

print(solution("987654321",2))