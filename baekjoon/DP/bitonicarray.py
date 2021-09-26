import sys
input = sys.stdin.readline

def solution(arr):
	up_cnt = [1] * len(arr)
	down_cnt = [1] * len(arr)
	for right in range(len(arr)):
		for left in range(right):
			if arr[left] < arr[right]:
				up_cnt[right] = max(up_cnt[right],up_cnt[left]+1)
	for right in range(len(arr)-1,-1,-1):
		for left in range(right-1,-1,-1):
			if arr[left] > arr[right]:
				down_cnt[left] = max(down_cnt[left],down_cnt[right]+1)
	answer = 0
	for i in range(len(arr)):
		answer = max(answer,up_cnt[i]+down_cnt[i]-1)

	return answer
if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split()))
	print(solution(arr))