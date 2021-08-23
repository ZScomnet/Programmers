def solution(str1,str2):
	str1=str1.upper()
	str2=str2.upper()
	str1_set = []
	str2_set = []

	for s1 in range(len(str1)-1):
		if 'A' <= str1[s1] <= 'Z' and 'A' <= str1[s1+1] <= 'Z':
			str1_set.append(str1[s1]+str1[s1+1])
	for s2 in range(len(str2)-1):
		if 'A' <= str2[s2] <= 'Z' and 'A' <= str2[s2+1] <= 'Z':
			str2_set.append(str2[s2]+str2[s2+1])

	join_set = []

	for s1 in str1_set:
		for i in range(len(str2_set)):
			if s1 == str2_set[i]:
				join_set.append(s1)
				del str2_set[i]
				break
	union_set = str1_set + str2_set
	if len(union_set) == 0:
		answer = 65536
	else:
		answer = int(len(join_set)/len(union_set)*65536)

	return answer

if __name__ == '__main__':
	print(solution("FRANCE","french"))