import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	left,right = [],[]
	mid = int(input())
	print(mid)
	for _ in range(1,N):
		num = int(input())
		if len(left) == len(right):
			if mid > num:
				heapq.heappush(left,-num)
				heapq.heappush(right,mid)
			else:
				heapq.heappush(left,-mid)
				heapq.heappush(right,num)
			mid = -heapq.heappop(left)
		else:
			if mid > num:
				heapq.heappush(left,-num)
			else:
				heapq.heappush(left,-mid)
				heapq.heappush(right,num)
				mid = heapq.heappop(right)
		print(mid)	