import sys
input = sys.stdin.readline

def solution():
	T = int(input())
	for t in range(T):
		N = int(input())
		num = list(map(int,input().split()))
		cnt,oneCnt = 0,0
		for i in range(N):
			if num[i] == 1:
				oneCnt += 1
			else:
				cnt += oneCnt
		answer = cnt
		leftIdx,rightIdx = -1,-1
		for i in range(N):
			if num[i] == 0:
				leftIdx = i
				break
		for i in range(N-1,-1,-1):
			if num[i] == 1:
				rightIdx = i
				break
		num[leftIdx] = 1
		cnt,oneCnt = 0,0
		for i in range(N):
			if num[i] == 1:
				oneCnt += 1
			else:
				cnt += oneCnt
		answer = max(cnt,answer)
		num[leftIdx] = 0
		num[rightIdx] = 0
		cnt,oneCnt = 0,0
		for i in range(N):
			if num[i] == 1:
				oneCnt += 1
			else:
				cnt += oneCnt
		answer = max(answer,cnt)
		print(answer)


if __name__ == "__main__":
	solution()
