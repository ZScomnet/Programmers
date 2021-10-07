import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	q = deque()
	for _ in range(N):
		line = input().split()
		if line[0] == 'push':
			q.append(line[1])
		elif line[0] == 'front':
			if len(q) == 0:
				print(-1)
			else:
				print(q[0])
		elif line[0] == 'pop':
			if len(q) == 0:
				print(-1)
			else:
				print(q.popleft())
		elif line[0] == 'size':
			print(len(q))
		elif line[0] == 'empty':
			if len(q) == 0:
				print(1)
			else:
				print(0)
		elif line[0] == 'back':
			if len(q) == 0:
				print(-1)
			else:
				print(q[-1])