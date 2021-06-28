def solution(clothes):
	table = [1 for _ in range(1000000)]
	add = []
	for i in clothes:
		data = hash(i[1]) % 1000000
		if data not in add:
			add.append(data)
		table[data] += 1
	result = 1
	for i in add:
		result *= table[i]
	
	return result-1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))