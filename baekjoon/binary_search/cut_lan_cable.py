import sys
input = sys.stdin.readline

def solution(cables,N):
	left,right = 0,2**31-1
	answer = 1
	while left<=right:
		mid = (left+right) // 2
		cnt = 0
		for cable in cables:
			cnt += cable//mid
		if cnt >= N and answer < mid:
			answer = mid
			left = mid+1
		elif cnt < N:
			right = mid-1
		elif cnt >= N:
			left = mid+1

	return answer


if __name__ == "__main__":
	K,N = map(int,input().split())
	cables = []
	for _ in range(K):
		cables.append(int(input()))
	print(solution(sorted(cables),N))