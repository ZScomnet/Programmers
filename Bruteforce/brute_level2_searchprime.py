from itertools import permutations
def solution(numbers):
	all_number = set()
	for i in range(1,len(numbers)+1):
		all_number |= set(int(''.join(j)) for j in permutations(list(numbers),i))

	result = set()
	if 2 in all_number:
		result.add(2)
	if 3 in all_number:
		result.add(3)
	for i in all_number:
		if i%2 == 0 or i < 4:
			continue
		is_prime = True
		for k in range(3,int(i**(1/2))+1,2):
			if i == 25:
				print(i,k,i%k)
			if i%k == 0:
				is_prime = False
				break
		if is_prime or i == 2:
			result.add(i)
	return len(result)


print(solution("12345"))