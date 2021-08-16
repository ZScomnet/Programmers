def solution(scores):
	stu_score = [[scores[col][row] for col in range(len(scores))] for row in range(len(scores))]
	result = ""
	for student in range(len(stu_score)):
		avr = 0
		max_score = max(stu_score[student])
		min_score = min(stu_score[student])
		if stu_score[student].count(max_score) == 1 and stu_score[student][student] == max_score:
			stu_score[student][student] = 0
			avr = sum(stu_score[student]) / (len(scores)-1)
		elif stu_score[student].count(min_score) == 1 and stu_score[student][student] == min_score:
			stu_score[student][student] = 0
			avr = sum(stu_score[student]) / (len(scores)-1)
		else:
			avr = sum(stu_score[student]) / len(scores)

		if avr >= 90:
			result += "A"
		elif avr >= 80:
			result += "B"
		elif avr >= 70:
			result += "C"
		elif avr >= 50:
			result += "D"
		else:
			result += "F"
	return result

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))