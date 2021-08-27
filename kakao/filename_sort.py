def solution(files):
	answer = []
	for file in files:
		head,num,tail = "","",""
		number = False
		for l in range(len(file)):
			if file[l].isdigit():
				num += file[l]
				number = True
			elif not number:
				head += file[l]
			else:
				tail += file[l:]
				break
		answer.append((head,num,tail))
	answer.sort(key=lambda x:(x[0].lower(),int(x[1])))

	return [''.join(i) for i in answer]

if __name__ == "__main__":
	print(solution(["A09-","A08-","A007-","A0006-","a00005-","A00004-"]))