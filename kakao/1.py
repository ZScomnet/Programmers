def solution(id_list,report,k):
	dic_point = dict()
	dic_report = dict()
	answer = []
	for i in id_list:
		dic_point[i] = 0
		dic_report[i] = []

	for s in report:
		r,b = s.split()
		if b not in dic_report[r]:
			dic_point[b] += 1
			dic_report[r].append(b)
	for key,value in zip(dic_report.keys(),dic_report.values()):
		result = 0
		for name in value:
			if dic_point[name] >= k:
				result += 1

		answer.append(result)

	return answer

if __name__ == "__main__":
	print(solution(["con", "ryan","appech"],["ryan con","con ryan","appech ryan","appech con"],2))