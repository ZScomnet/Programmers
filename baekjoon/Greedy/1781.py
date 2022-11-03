import sys
import heapq
from collections import deque
input = sys.stdin.readline

def solution():
	N = int(input())
	cup = []
	for _ in range(N):
		deadline, ramen = map(int,input().split())
		cup.append([deadline,-ramen])
	cup = deque(sorted(cup))

	q = []
	time = 0
	while cup:
		deadline, ramen = cup.popleft()
		if deadline > time: # 같은 시간 중 가장 보상이 큰 문제 풀기
			heapq.heappush(q, -ramen)
			time += 1
		elif q and q[0] < -ramen: # 풀어온 문제보다 보상이 좋은 경우 해당 문제 채택
			heapq.heappop(q)
			heapq.heappush(q, -ramen)
	return sum(q)

if __name__ == "__main__":
	print(solution())