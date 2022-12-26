import sys
input = sys.stdin.readline

def solution():
	N, M = map(int,input().split())
	a = list(map(int,input().split()))
	answer = 0
	left,right = 0,0
	s = 0
	while left < len(a):
		if s <= M:
			answer = max(answer,s)
		if s <= M and right < len(a):
			s += a[right]
			right += 1
		else:
			s -= a[left]
			left += 1
	print(answer)

if __name__ == "__main__":
	solution()