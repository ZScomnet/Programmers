import sys
input = sys.stdin.readline

def solution(hubs,C):
	left,right = 1,hubs[-1]
	answer = 0
	while left <= right:
		mid = (left+right)//2
		before = hubs[0]
		cnt = 1
		for i in range(1,len(hubs)):
			if hubs[i] >= before+mid:
				cnt+=1
				before = hubs[i]
		if cnt >= C:
			left = mid + 1
			answer = mid
		else:
			right = mid - 1
	return answer

if __name__ == "__main__":
	N,C = map(int,input().split())
	hubs = []
	for _ in range(N):
		hubs.append(int(input()))
	print(solution(sorted(hubs),C))