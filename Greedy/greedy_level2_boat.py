def solution(people, limit):
	people.sort()
	result = 0
	left = 0
	right = len(people) - 1
	while left < right:
		if people[left] + people[right] <= limit:
			left += 1
		right -= 1
		result += 1
	if left == right:
		result += 1
	
	return result

print(solution([10,20,30],100))