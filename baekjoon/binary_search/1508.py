def solution():
	N,M,K = map(int,input().split())
	spot = list(map(int,input().split()))
	left,right = 0,spot[-1]-spot[0]
	pivot = 0
	while left <= right:
		mid = (left+right) // 2
		cnt = 1
		idx = spot[0]
		for i in range(1,K):
			if spot[i] - idx >= mid:
				idx = spot[i]
				cnt += 1
		if cnt >= M:
			pivot = mid
			left = mid + 1
		else:
			right = mid - 1
	answer = "1"
	cnt = 1
	idx = spot[0]
	for i in range(1,K):
		if cnt < M and spot[i] - idx >= pivot:
			answer += '1'
			cnt += 1
			idx = spot[i]
		else:
			answer += '0'
	return answer

if __name__ == "__main__":
	print(solution())