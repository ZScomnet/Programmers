import sys
from collections import deque

input = sys.stdin.readline

def solution(command,array):
	way = 1
	if array[0] == '':
		array.popleft()
	for i in command:
		if i == 'R':
			way *= -1
		else:
			if len(array) == 0:
				return 'error'
			else:
				if way == 1:
					array.popleft()
				else:
					array.pop()
	answer = "["
	for i in range(len(array)):
		if way == 1:
			answer += array[i]
		else:
			answer += array[-1+way*i]
		if i != len(array)-1:
			answer += ","
	return answer+"]"

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		command = input()
		n = int(input())
		array = deque(list(input()[1:-2].split(',')))
		print(solution(command[:-1],array))