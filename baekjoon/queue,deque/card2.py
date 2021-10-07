from collections import deque

if __name__ == "__main__":
	N = int(input())
	q = deque([i+1 for i in range(N)])
	while len(q) > 1:
		q.popleft()
		q.append(q.popleft())
	print(q.pop())