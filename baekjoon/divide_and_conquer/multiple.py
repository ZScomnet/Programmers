def solution(A,B,C):
	if C == 1:
		return 0
	else:
		stack = []
		while B > 1:
			if B % 2 == 0:
				stack.append(1)
			else:
				stack.append(A)
			A = (A%C) * (A%C)
			B = B // 2
		for i in stack:
			A = (i*A)%C
		return A % C

if __name__ == "__main__":
	A,B,C = map(int,input().split())
	print(solution(A,B,C))