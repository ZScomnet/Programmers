def solution(N,K):
	left,right = 1,K
	answer = 0
	while left <= right:
		mid = (left+right) // 2
		cnt = 0
		for i in range(1,N+1):
			cnt += min(N,mid//i)
		if cnt >= K:
			answer = mid
			right = mid-1
		else:
			left = mid+1

	return answer

if __name__ == "__main__":
	N = int(input())
	K = int(input())
	print(solution(N,K))