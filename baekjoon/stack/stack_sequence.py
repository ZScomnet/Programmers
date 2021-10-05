import sys
input = sys.stdin.readline

def solution(sequence):
	result = []
	stack = []
	for i in range(1,len(sequence)+1):
		result.append('+')
		stack.append(i)
		while sequence[-1] == stack[-1]:
			result.append('-')
			stack.pop()
			sequence.pop()
			if len(sequence) == 0 or len(stack) == 0:
				break
	if len(sequence) != 0:
		return ["NO"]

	return result
if __name__ == "__main__":
	N = int(input())
	sequence = []
	for _ in range(N):
		sequence.append(int(input()))
	result = solution(sequence[::-1])
	for i in result:
		print(i)