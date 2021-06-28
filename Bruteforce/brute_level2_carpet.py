def solution(brown,yellow):
	for i in range(3,int(brown/2)):
		if (brown+yellow) % i != 0:
			continue 
		brown_col = int((brown+yellow)/i) - 2
		if brown-2*i >= brown_col*2:
			return [int((brown+yellow)/i),i]

	return -1

print(solution(24,24))