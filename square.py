def cut(w,h):
	answer = 0
	start = 0
	term = h/w
	before = 0
	for _ in range(w):
		start += term
		if int(start) < start:
			answer += int(start)+1-before
		else:
			answer += int(start)-before
		before = int(start)
	return (w*h)-answer

def divide(w,h):
	if w%2 == 0 and h%2 == 0:
		result = divide(w//2,h//2)
		return [result[0]*2,result[1]+1]
	else:
		return [cut(w,h),0]

def solution(w,h):
	result = divide(w,h)
	answer = 0
	for i in range(1,result[1]+1):
		w = w // 2
		h = h // 2
		answer += (2**i)*w*h
	return answer + result[0]

if __name__ == "__main__":
	w = int(input())
	h = int(input())
	print(solution(w,h))