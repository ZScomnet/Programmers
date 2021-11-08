import sys
input = sys.stdin.readline

def solution(trees,M):
	left,right = 0,2000000000
	answer = 0
	while left <= right:
		mid = (left+right) // 2
		result = 0
		for tree in trees:
			if tree >= mid:
				result += tree - mid
		if result >= M and answer < mid:
			answer = mid
		elif result < M:
			right = mid-1
		elif result >= M:
			left = mid+1

	return answer

if __name__ == "__main__":
	N,M = map(int,input().split())
	trees = sorted(list(map(int,input().split())))
	print(solution(trees,M))