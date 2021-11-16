import sys
import heapq

input = sys.stdin.readline

def Solution(N):
	line = []
	for _ in range(N):
		num,a,b,c = map(int,input().split())
		heapq.heappush(line,(a*b*c,a+b+c,num))
	
	for _ in range(3):
		print(heapq.heappop(line)[2],end=" ")


if __name__ == "__main__":
	N = int(input())
	Solution(N)