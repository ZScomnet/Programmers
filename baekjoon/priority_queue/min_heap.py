import sys
import heapq
input = sys.stdin.readline

def solution(N):
	line = []
	for _ in range(N):
		num = int(input())
		if num == 0:
			if len(line) == 0:
				print(0)
			else:
				print(heapq.heappop(line))
		else:
			heapq.heappush(line,num)

if __name__ == "__main__":
	N = int(input())
	solution(N)