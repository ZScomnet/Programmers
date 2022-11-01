import sys
input = sys.stdin.readline

def solution():
	N = int(input())
	a = list(map(int,input().split()))
	answer = 0
	for i in range(N-2):
		if a[i+1] > a[i+2]:
			h = min(a[i],a[i+1]-a[i+2])
			answer += h*5
			a[i],a[i+1] = a[i]-h,a[i+1]-h
		h = min(a[i],a[i+1],a[i+2])
		answer += h*7
		a[i],a[i+1],a[i+2] = a[i]-h,a[i+1]-h,a[i+2]-h
		if a[i] > 0:
			answer += a[i]*3
			a[i] = 0
	h = min(a[-2],a[-1])
	answer += h*5
	answer += (max(a[-2],a[-1])-h)*3

	return answer

if __name__ == "__main__":
	print(solution())