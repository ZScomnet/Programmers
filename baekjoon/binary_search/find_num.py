import sys
input = sys.stdin.readline
def solution(N,find):
    left,mid,right = 0,N//2,N-1
    while left < right:
    	if num[mid] == find:
    		break
    	else:
    		if num[mid] > find:
    			right = mid-1
    		else:
    			left = mid+1
    		mid = (left+right)//2
    if num[mid] == find:
    	print(1)
    else:
    	print(0)

if __name__ == "__main__":
	N = int(input())
	num = sorted(list(map(int,input().split())))
	F = int(input())
	find = map(int,input().split())
	for i in find:
		solution(N,i)