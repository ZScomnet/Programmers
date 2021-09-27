import sys
input = sys.stdin.readline

def solution(cables):
	cables = sorted(cables,key=lambda x : x[0])
	arr = [cables[i][1] for i in range(len(cables))]
	cnt = [1] * len(arr)
	for right in range(len(arr)):
		for left in range(right):
			if arr[left] < arr[right]:
				cnt[right] = max(cnt[right],cnt[left]+1)

	return len(cables)-max(cnt)

if __name__ == "__main__":
	N = int(input())
	cables = []
	for _ in range(N):
		cable = list(map(int,input().split()))
		cables.append(cable)
	print(solution(cables))