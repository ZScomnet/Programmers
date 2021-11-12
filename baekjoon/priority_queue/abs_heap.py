import sys
import heapq

def solution(N):
	line = []
	for _ in range(N):
		num = int(input())
		if num == 0:
			if len(line) == 0:
				print(0)
			else:
				print(heapq.heappop(line)[1])
		else:
			if num < 0:
				heapq.heappush(line,(-num,num))
			else:
				heapq.heappush(line,(num,num))


if __name__ == "__main__":
	N = int(input())
	solution(N)