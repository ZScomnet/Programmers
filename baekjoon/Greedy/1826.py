from collections import deque
import heapq
import sys
input = sys.stdin.readline
def solution():
	N = int(input())
	oilbank = deque()
	for _ in range(N):
		oilbank.append(list(map(int,input().split())))
	oilbank = deque(sorted(oilbank))
	L,P = map(int,input().split())
	answer = 0
	q = []
	while True:
		while oilbank:
			if oilbank[0][0] <= P:
				length, oil = oilbank.popleft()
				heapq.heappush(q,-1*oil)
			else:
				break
		if L <= P:
			break
		else:
			if q:
				P -= heapq.heappop(q)
				answer += 1
			else:
				answer = -1
				break
	return answer
if __name__ == "__main__":
	print(solution())