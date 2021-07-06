def solution(money):
	first = [0 for _ in range(len(money))]
	first[0] = money[0]
	first[1] = max(money[0],money[1])

	for i in range(2,len(money)-1):
		first[i] = max(first[i-1],money[i]+first[i-2])

	second = [0 for _ in range(len(money))]
	second[1] = money[1]
	second[2] = max(money[1],money[2])

	for i in range(3,len(money)):
		second[i] = max(second[i-1],money[i]+second[i-2])

	return max(first[-2],second[-1])

print(solution([1, 1, 4, 1, 4]))