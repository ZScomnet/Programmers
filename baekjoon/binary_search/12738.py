import sys
input = sys.stdin.readline

def solution():
	N = int(input())
	num = list(map(int,input().split()))
	lis = []
	for i in num: 
		if len(lis) == 0:
			lis.append(i)
		else:
			left,right = 0,len(lis)
			while left < right:
				mid = (left+right) // 2
				if lis[mid] < i:
					left = mid+1
				else:
					right = mid
			if left >= len(lis)-1:
				if lis[-1] < i:
					lis.append(i)
				elif i < lis[-1]:
					lis[-1] = i
			else:
				lis[left] = min(lis[left],i)

	return len(lis)

if __name__ == "__main__":
	print(solution())