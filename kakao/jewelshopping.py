def solution(gems):
	goal = len(set(gems))
	if goal == 1:
		return [1,1]
	left,right = 0,1
	result = [1,len(gems)]
	data = dict()
	data[gems[left]] = 1
	before = 0
	while left < right:
		try:
			if before != right:
				data[gems[right]] += 1
				before = right
		except KeyError:
			data[gems[right]] = 1
			before = right
		if len(data) == goal and right-left < result[1]-result[0]:
			result = [left+1,right+1]
		if right < len(gems)-1 and len(data) != goal:
			right += 1
		else:
			data[gems[left]] -= 1
			if data[gems[left]] == 0:
				del data[gems[left]]
			left += 1
	return result


print(solution(["A","B","B","B","B","B","B","C","B","A"]))

# ["A","A","A","B","B"] [3,4]
# ["A"] [1,1]
# ["A","B","B","B","B","B","B","C","B","A"] [8,10]