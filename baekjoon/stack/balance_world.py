import sys
input = sys.stdin.readline

def solution(line):
	stack = []
	for i in line:
		if len(stack) == 0 and (i == ')'or i == ']'):
			return "no"
		elif i in ['(',')','[',']']:
			if i == '(' or i == '[':
				stack.append(i)
			elif i == ')' and stack[-1] == '(':
				stack.pop()
			elif i == ']' and stack[-1] == '[':
				stack.pop()
			else:
				return "no"
	if len(stack) == 0:
		return "yes"
	else:
		return "no"

if __name__ == "__main__":
	while True:
		line = input()
		if line[:-1] == '.':
			break
		print(solution(line[:-1]))