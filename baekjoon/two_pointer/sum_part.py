import sys
input = sys.stdin.readline

def solution(N,S,num):
	now = num[0]
	left,right = 0,0
	answer = 100001
	while left <= right:
		if now >= S:
			answer = min(answer,right-left+1)
		if now < S and right < N-1:
			right += 1
			now += num[right]
		else:
			now -= num[left]
			left += 1
	if answer != 100001:
		return answer
	else:
		return 0

if __name__ == "__main__":
	N,S = map(int,input().split())
	num = list(map(int,input().split()))
	print(solution(N,S,num))