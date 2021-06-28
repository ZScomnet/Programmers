def solution(citations):
	citations.sort()
	result = 0
	for i in range(1,len(citations)+1):
		for k in range(len(citations)):
			if citations[k] >= i and len(citations[k:]) >= i:
				result = i
				break
	return result

print(solution([0, 0, 1, 1] ))