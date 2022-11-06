import heapq
import sys
input = sys.stdin.readline

def solution():
	N,L = map(int,input().split())
	q = []
	for _ in range(N):
		heapq.heappush(q,list(map(int,input().split())))

	answer = 0
	last = -1
	while q:
		start,end = heapq.heappop(q)
		if start <= last <= end-1:
			start = last
		elif end <= last:
			continue
		length = end-start
		bridge = ( length // L )
		if length % L > 0:
			bridge += 1
		answer += bridge
		last = start + L * bridge
	return answer

if __name__ == "__main__":
	print(solution())