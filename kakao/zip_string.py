def solution(msg):
	dic = dict()
	for i in range(26):
		dic[chr(ord('A')+i)] = i+1
	answer = []
	w = ""
	for c in msg:
		if w+c not in dic:
			dic[w+c] = len(dic)+1
			answer.append(dic[w])
			w = c
		else:
			w += c
	if w not in dic:
		dic[w] = len(dic)+1
	answer.append(dic[w])

	return answer

if __name__ == "__main__":
	print(solution("ABABABABABABABAB"))