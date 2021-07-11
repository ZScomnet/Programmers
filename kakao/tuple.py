def solution(s):
	before = 0
	s_set = set()
	counter = [0] * 100001
	for lit in s:
		if '0' <= lit <= '9':
			before *= 10
			before += int(lit)
		elif before != 0:
			counter[before] += 1
			s_set.add(before)
			before = 0
	result = [0] * len(s_set)
	for i in s_set:
		result[counter[i]-1] = i
	result.reverse()
	return result
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))