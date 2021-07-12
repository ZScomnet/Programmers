def solution(s):
	stack = []
	for lit in s:
		if len(stack) == 0:
			stack.append(lit)
		elif stack[-1] == lit:
			stack.pop()
		else:
			stack.append(lit)

	if len(stack) == 0:
		return 1
	else:
		return 0

print(solution("cdcd"))