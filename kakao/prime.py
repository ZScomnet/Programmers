def solution(n, k):
	num = ""
	while n != 0:
		num = str(n%k) + num
		n = n // k
	num = num.split("0")
	answer = 0
	for i in num:
		is_prime = False
		if i == "":
			continue
		if int(i) == 2:
			answer += 1
			continue
		if int(i) % 2 == 0 or int(i) == 1:
			continue
		for k in range(3,int(int(i)**(1/2))+1,2):
			if int(i) % k == 0:
				is_prime = True
				break
		if is_prime:
			continue
		answer += 1 

	return answer

if __name__ == "__main__":
	print(solution(110011, 10))