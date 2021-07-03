def solution(triangle):
	result = 0
	for line in range(1,len(triangle)):
		for num in range(0,len(triangle[line])):
			if num == 0:
				triangle[line][0] += triangle[line-1][0]
			elif num == len(triangle[line])-1:
				triangle[line][num] += triangle[line-1][num-1]
			else:
				if triangle[line-1][num-1] > triangle[line-1][num]:
					triangle[line][num] += triangle[line-1][num-1]
				else:
					triangle[line][num] += triangle[line-1][num]
			if result < triangle[line][num]:
				result = triangle[line][num]

	return result

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))