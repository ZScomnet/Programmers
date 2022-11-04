from collections import deque
import heapq
import sys
input = sys.stdin.readline

def solution():
	N,K = map(int,input().split())
	jewel = []
	bag = []
	answer = 0
	for _ in range(N):
		m,v = map(int,input().split())
		jewel.append([m,-v])
	for _ in range(K):
		bag.append(int(input()))
	jewel = deque(sorted(jewel))
	bag = sorted(bag)
	q = []
	for i in bag:
		while jewel:
			m,v = jewel.popleft()
			if m <= i:
				heapq.heappush(q,v)
			else:
				jewel.appendleft([m,v])
				break
		if q:
			answer += -1 * heapq.heappop(q)

	return answer

if __name__ == "__main__":
	print(solution())