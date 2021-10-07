import sys
from collections import deque

if __name__ == '__main__':
	N = int(input())
	q = deque()
	for _ in range(N):
		line = input().split()
		if line[0] == 'push_front':
			q.appendleft(line[1])
		elif line[0] == 'push_back':
			q.append(line[1])
		elif line[0] == 'pop_front':
			if len(q) == 0:
				print(-1)
			else:
				print(q.popleft())
		elif line[0] == 'pop_back':
			if len(q) == 0:
				print(-1)
			else:
				print(q.pop())
		elif line[0] == 'size':
			print(len(q))
		elif line[0] == 'empty':
			if len(q) == 0:
				print(1)
			else:
				print(0)
		elif line[0] == 'front':
			if len(q) == 0:
				print(-1)
			else:
				print(q[0])
		elif line[0] == 'back':
			if len(q) == 0:
				print(-1)
			else:
				print(q[-1])