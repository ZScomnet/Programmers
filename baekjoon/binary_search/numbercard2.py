import sys
input = sys.stdin.readline

def solution(cards,find):
	left,mid,right = 0,len(cards)//2,len(cards)-1
	answer = 0
	while left < right:
		if cards[mid] == find:
			break
		else:
			if cards[mid] > find:
				right = mid-1
			else:
				left = mid+1
			mid = (left+right)//2
	if cards[mid] == find:
		return mid
	else:
		return -1
if __name__ == "__main__":
	N = int(input())
	cards = list(map(int,input().split()))
	dic = dict()
	for i in cards:
		if i not in dic:
			dic[i] = 1
		else:
			dic[i] += 1
	cards = sorted(dic.keys())
	F = int(input())
	find = map(int,input().split())
	for i in find:
		idx = solution(cards,i)
		if idx == -1:
			print(0,end=" ")
		else:
			print(dic[cards[idx]],end=" ")