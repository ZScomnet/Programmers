def solution(n,k):
	line = []
	answer = 0
	while n != 0:
		line.append(str(n%k))
		n = n//k

	num = ''.join(line[::-1])
	num = num.split('0')
	for i in num:
		if i == '':
			continue
		if int(i) == 2:
			answer += 1
		elif int(i) % 2 == 0 or int(i) == 1:
			continue
		else:
			is_prime = True
			for idx in range(3,int(int(i)**0.5)+1,2):
				if int(i) % idx == 0:
					is_prime = False
					break
			if is_prime:
				answer += 1

	return answer
if __name__ == "__main__":
	print(solution(110011,10))