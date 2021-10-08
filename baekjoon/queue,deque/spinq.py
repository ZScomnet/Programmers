from collections import deque

def solution(N,line):
	answer = 0
	q = deque([i+1 for i in range(N)])
	for num in line:
		move = 0
		for idx in range(len(q)):
			if q[idx] == num:
				move = idx
				break
			elif q[-1*idx] == num:
				move = -1*idx
				break
		if move < 0:
			answer += -1*move
			for _ in range(-1*move):
				q.appendleft(q.pop())
		else:
			answer += move
			for _ in range(move):
				q.append(q.popleft())
		q.popleft()
	return answer

if __name__ == "__main__":
	N,M = map(int,input().split())
	line = list(map(int,input().split()))
	print(solution(N,line))