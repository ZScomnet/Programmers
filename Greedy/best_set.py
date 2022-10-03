def solution(n, s):
	if s // n == 0:
		return [-1]
	answer = [s//n]*n
	cnt = s%n
	while cnt > 0:
		answer[-1-cnt+1] += 1
		cnt -= 1
	return answer

if __name__ == "__main__":
	print(solution(2,9))	