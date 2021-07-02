def solution(distance,rocks,n):
	rocks = sorted(rocks) + [distance]
	left,right = 0,distance
	center = (left+right) // 2
	while left <= right:
		cnt = 0
		prev = 0
		for i in rocks:
			if i - prev < center:
				cnt += 1
			else:
				prev = i
		if cnt <= n:
			left = center+1
		else:
			right = center-1
		center = (left+right) // 2

	return center

print(solution(25,[2,14,11,21,17],2))