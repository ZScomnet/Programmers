def solution(line):
	data = line.split('-')
	answer = 0
	num = data[0].split('+')
	for n in range(len(num)):
		answer += int(num[n])
	for i in range(1,len(data)):
		num = data[i].split('+')
		minus = 0
		for n in range(len(num)):
			minus += int(num[n])
		answer -= minus
	return answer

if __name__ == "__main__":
	print(solution(str(input())))