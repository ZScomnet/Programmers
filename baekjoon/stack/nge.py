def solution(line):
	answer = [-1] * len(line)
	stack = [0]
	for i in range(1,len(line)):
		while line[stack[-1]] < line[i]:
			answer[stack[-1]] = i
			stack.pop()
			if len(stack) == 0:
				break
		stack.append(i)

	for i in range(len(answer)):
		if answer[i] != -1:
			print(line[answer[i]],end=" ")
		else:
			print(-1,end=" ")
	print()
	
if __name__ == "__main__":
	N = int(input())
	line = list(map(int,input().split()))
	solution(line)