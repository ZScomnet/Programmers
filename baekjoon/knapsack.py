import sys
from itertools import combinations
input = sys.stdin.readline

# MITM (Meet in the middle) Algorithm
def solution(N,C,m):
	if N == 1 and m[0] <= C:
		return 2
	if N == 1 and m[0] > C:
		return 1

	left_m,right_m = m[:N//2], m[N//2:]
	sub_left,sub_right = [0],[0]
	
	for i in range(1,len(left_m)+1):
		for sub in combinations(left_m,i):
			sub_left.append(sum(sub))
	sub_left = sorted(sub_left)

	for i in range(1,len(right_m)+1):
		for sub in combinations(right_m,i):
			sub_right.append(sum(sub))
	sub_right = sorted(sub_right)
	answer = 0
	for i in sub_right:
		if i > C:
			continue
		left = 0
		right = len(sub_left)
		while left < right:
			mid = (left+right) // 2
			if sub_left[mid]+i > C:
				right = mid
			else:
				left = mid+1
		answer += right

	return answer

if __name__ == "__main__":
	N,C = map(int,input().split())
	m = list(map(int,input().split()))
	print(solution(N,C,m))