import sys
input = sys.stdin.readline

def solution(N,s):
	s = sorted(s)
	left,right = 0,N-1
	L,R = 1000000000,1000000000
	while left < right:
		if abs(s[left]+s[right]) < abs(L+R):
			L,R = s[left],s[right]
		if s[left]+s[right] > 0:
			right -= 1
		else:
			left += 1
	print(L,R)



if __name__ == "__main__":
	N = int(input())
	s = list(map(int,input().split()))
	solution(N,s)