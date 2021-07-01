def solution(n,times):
	times = sorted(times)
	left,right = 1,times[-1]*n
	result = 0
	center = (left+right) // 2
	while left < right:
		for i in times:
			result += center // i
		
		if result >= n:
			right = center
		else:
			left = center+1
		result = 0
		center = (left+right) // 2
	return left

print(solution(6, [7, 10]))