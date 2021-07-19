def solution(n,works):
	work_hash = [0]*50001
	maximum = 0
	for work in works:
		work_hash[work] += 1
		if maximum < work:
			maximum = work

	while n > 0:
		work_hash[maximum] -= 1
		work_hash[maximum-1] += 1
		n -= 1
		if work_hash[maximum] == 0:
			maximum -= 1
		
	result = 0
	for i in range(1,maximum+1):
		result += work_hash[i] * i*i

	return result

print(solution(4,[4,3,3]))