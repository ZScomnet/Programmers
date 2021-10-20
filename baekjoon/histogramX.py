import sys
input = sys.stdin.readline

def solution(N,line):
	stack = []
	area = min(line)*N
	for i in line:
		if len(stack) == 0:
			stack.append(i)
		else:
			if stack[-1] <= i:
				stack.append(i)
			else:
				length = 1
				while stack:
					if stack[-1] <= i:
						break
					area = max(length*stack.pop(),area)
					length += 1
				if stack:
					for i in range(length):
						stack.append(stack[-1])
				else:
					stack.append(i)


	if stack:
		length = 1
		while stack:
			area = max(length*stack.pop(),area)
			length += 1

	for i in line[::-1]:
		if len(stack) == 0:
			stack.append(i)
		else:
			if stack[-1] <= i:
				stack.append(i)
			else:
				length = 1
				while stack:
					if stack[-1] <= i:
						break
					area = max(length*stack.pop(),area)
					length += 1
				if stack:
					for i in range(length):
						stack.append(stack[-1])
				else:
					stack.append(i)

	if stack:
		length = 1
		while stack:
			area = max(length*stack.pop(),area)
			length += 1

	return area

if __name__ == "__main__":
	while True:
		line = list(map(int,input().split()))
		if line[0] == 0:
			break
		print(solution(line[0],line[1:]))