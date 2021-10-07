from collections import deque

if __name__ == "__main__":
	N,K = map(int,input().split())
	q = deque([i+1 for i in range(N)])
	answer = "<"
	while q:
		if len(q) != N:
			answer += ", "
		for _ in range(K-1):
			q.append(q.popleft())
		answer += str(q.popleft())
	print(answer+">")