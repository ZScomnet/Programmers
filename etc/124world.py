def solution(n):
	answer = ""
	while n:
		if n % 3:
			answer = str(n%3) + answer
			n = n//3
		else:
			answer = "4" + answer
			n = n//3
			n -= 1

	return answer

if __name__ == "__main__":
	for i in range(1,30):
		print(solution(i))