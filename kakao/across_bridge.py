def solution(stones,k):
	left,right = 1,max(stones)
	result = 0
	while left <= right:
		center = (left+right) // 2
		cnt = 0
		for i in range(0,len(stones)):
			if stones[i] <= center:
				cnt += 1
			else:
				cnt = 0
			if cnt >= k:
				break
		if cnt < k:
			left = center + 1
		else:
			result = center
			right = center - 1
		
	return result

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))