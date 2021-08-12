def solution(n,s):
	if n > s:
		result = [-1]
	else:
		result = []
		for i in range(0,n):
			result.append(int(s/n))
		add_point = s%n
		for i in range(add_point):
			result[-1-i] += 1
	return result
print(solution(2,9))