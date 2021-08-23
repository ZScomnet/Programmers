def solution(n,arr1,arr2):
	answer = []
	for ar1,ar2 in zip(arr1,arr2):
		line = ""
		for i in range(n):
			if ar1 % 2 == 0 and ar2 % 2 == 0:
				line += ' '
			else:
				line += '#'
			ar1 = ar1 // 2
			ar2 = ar2 // 2
		answer.append(line[::-1])

	return answer

if __name__ == "__main__":
	print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))