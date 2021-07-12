def solution(expression):
	ex_split = []
	total_oper = [["+","-","*"],["+","*","-"],["-","+","*"],["-","*","+"],["*","+","-"],["*","-","+"]]
	before = 0
	for lit in expression:
		if '0' <= lit <= '9':
			before *= 10
			before += int(lit)
		else:
			ex_split.append(before)
			ex_split.append(lit)
			before = 0
	ex_split.append(before)
	result = 0
	for oper_list in total_oper:
		calculate = ex_split.copy()
		for oper in oper_list:
			op_index = 1
			while op_index < len(calculate):
				if calculate[op_index] == oper:
					if oper == '+':
						calculate[op_index-1] += calculate[op_index+1]
					elif oper == '*':
						calculate[op_index-1] *= calculate[op_index+1]
					else:
						calculate[op_index-1] -= calculate[op_index+1]
					del calculate[op_index+1]
					del calculate[op_index]
				else:
					op_index += 2
		if result < abs(calculate[0]):
			result = abs(calculate[0])
	return result

print(solution("50*6-3*2"))