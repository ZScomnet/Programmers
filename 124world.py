def solution(n):
	answer = ""
	while n:
		if n % 3 > 0:
			answer = str(n%3) + answer
		else:
			answer = "4" + answer
			if n <= 3:
				n = 0
		n = n // 3	
	return answer

if __name__ == "__main__":
	for i in range(1,16):
		print(solution(i))