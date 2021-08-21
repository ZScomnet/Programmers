def solution(info,query):
	dic = dict()
	for i1 in ['cpp','java','python','-']:
		for i2 in ['backend','frontend','-']:
			for i3 in ['junior','senior','-']:
				for i4 in ['pizza','chicken','-']:
					dic[i1+i2+i3+i4] = []
	for i in info:
		data = i.split()
		dic[data[0]+data[1]+data[2]+data[3]].append(int(data[4]))

		dic['-'+data[1]+data[2]+data[3]].append(int(data[4]))
		dic[data[0]+'-'+data[2]+data[3]].append(int(data[4]))
		dic[data[0]+data[1]+'-'+data[3]].append(int(data[4]))
		dic[data[0]+data[1]+data[2]+'-'].append(int(data[4]))

		dic['-'+'-'+data[2]+data[3]].append(int(data[4]))
		dic['-'+data[1]+'-'+data[3]].append(int(data[4]))
		dic['-'+data[1]+data[2]+'-'].append(int(data[4]))
		dic[data[0]+'-'+'-'+data[3]].append(int(data[4]))
		dic[data[0]+'-'+data[2]+'-'].append(int(data[4]))
		dic[data[0]+data[1]+'-'+'-'].append(int(data[4]))

		dic['-'+'-'+'-'+data[3]].append(int(data[4]))
		dic['-'+'-'+data[2]+'-'].append(int(data[4]))
		dic['-'+data[1]+'-'+'-'].append(int(data[4]))
		dic[data[0]+'-'+'-'+'-'].append(int(data[4]))

		dic['-'+'-'+'-'+'-'].append(int(data[4]))
	for i1 in ['cpp','java','python','-']:
		for i2 in ['backend','frontend','-']:
			for i3 in ['junior','senior','-']:
				for i4 in ['pizza','chicken','-']:
					dic[i1+i2+i3+i4].sort()

	answer = []
	for q in query:
		data = q.split()
		result = len(dic[data[0]+data[2]+data[4]+data[6]])
		for score in dic[data[0]+data[2]+data[4]+data[6]]:
			if int(score) >= int(data[7]):
				break
			result -= 1
		answer.append(result)

	return answer

if __name__ == "__main__":
	print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))