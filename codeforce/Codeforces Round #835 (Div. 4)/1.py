import sys
input = sys.stdin.readline

def solution():
	N = int(input())
	for _ in range(N):
		num = sorted(list(map(int,input().split())))
		print(num[1])
if __name__ == "__main__":
	solution()