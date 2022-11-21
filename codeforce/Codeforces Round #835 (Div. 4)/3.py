import sys
input = sys.stdin.readline

def solution():
	T = int(input())
	for t in range(T):
		N = int(input())
		num = list(map(int,input().split()))
		first, second = 0,0
		for i in num:
			if i >= first:
				second = first
				first = i
			elif i >= second:
				second = i
		for i in range(N):
			if num[i] == first:
				num[i] -= second
			else:
				num[i] -= first
		for i in num:
			print(i,end=' ')
		print()
if __name__ == "__main__":
	solution()
