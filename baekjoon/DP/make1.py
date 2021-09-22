import sys
from collections import deque
input = sys.stdin.readline

def solution(N):
	if N == 1:
		return 0
	elif N <= 3:
		return 1
	else:
		answer = 1
		q = deque()
		memory = [0]*(N+1)
		q.append(1)
		new_q = deque()
		while q:
			num = q.popleft()
			if num+1 <= N:
				if memory[num+1] == 0:
					memory[num+1] = answer
					new_q.append(num+1)
			if num*2 <= N:
				if memory[num*2] == 0:
					memory[num*2] = answer
					new_q.append(num*2)
			if num*3 <= N:
				if memory[num*3] == 0:
					memory[num*3] = answer
					new_q.append(num*3)
			if memory[N] != 0:
				break
			if len(q) == 0:
				q = new_q
				new_q = deque()
				answer += 1

		return memory[N]

if __name__ == "__main__":
	N = int(input())
	print(solution(N))