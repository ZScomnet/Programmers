from itertools import combinations

def solution(numbers,target):
	numbers = sorted(numbers)
	default = sum(numbers)
	result = 0
	for i in range(1,len(numbers)):
		cal_list = list(combinations(numbers,i))
		for d in cal_list:
			if target == default - sum(d)*2:
				result += 1
	return result

print(solution([1,1,1,1,1],3))