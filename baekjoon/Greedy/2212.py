import sys
input = sys.stdin.readline

def solution():
	N = int(input())
	K = int(input())
	c = list(map(int,input().split()))
	if N-K <= 0:
		return 0
	c.sort()
	length = []
	for i in range(1,N):
		length.append(c[i]-c[i-1])
	length.sort()
	return sum(length[:N-K])


if __name__ == "__main__":
	print(solution())