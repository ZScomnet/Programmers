from collections import deque

def solution(N,K):
	answer = 0
	q = deque()
	counter = [0] * 100001
	counter[N] = 1
	q.append(N)
	if N == K:
		return 0
	while q:
		answer += 1
		next_q = deque()
		while q:
			now = q.popleft()
			for idx in [-1,1]:
				if 0 <= now+idx < 100001:
					if counter[now+idx] == 0:
						next_q.append(now+idx)
						counter[now+idx] += 1
					if now+idx == K:
						return answer
			if 0 <= now*2 < 100001:
				if counter[now*2] == 0:
					next_q.append(now*2)
					counter[now*2] += 1
				if now*2 == K:
					return answer
		q = next_q

if __name__ == "__main__":
	N,K = map(int,input().split())
	print(solution(N,K))