import heapq
import sys
input = sys.stdin.readline

def solution():
	N,C = map(int,input().split())
	M = int(input())
	delivery = []
	city = [C] * N
	answer = 0
	for _ in range(M):
		start,end,m = map(int,input().split())
		heapq.heappush(delivery,[end,start,m])
	while delivery:
		end,start,m = heapq.heappop(delivery)
		d = min(city[start-1:end])
		d = min(d,m)
		if d == 0:
			continue
		else:
			answer += d
			for i in range(start-1,end-1):
				city[i] -= d

	return answer

if __name__ == "__main__":
	print(solution())