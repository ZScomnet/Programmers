import sys
input = sys.stdin.readline

def solution():
	N = int(input())
	l = list(map(int,input().split()))
	left,right = 0,N-1
	mid_l = l[left]+l[right]
	L,R = 0,N-1
	while left < right:
		mid = l[left]+l[right]
		if abs(mid) < abs(mid_l):
			L,R = left,right
			mid_l = mid 
		if mid > 0:
			right -= 1
		elif mid < 0:
			left += 1
		else:
			break
	print(l[L],l[R])

if __name__ == "__main__":
	solution()