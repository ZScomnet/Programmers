import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

tree = []
result = []

def solution(left,right):
	if left > right:
		return
	else:
		pivot = right+1
		for mid in range(left+1,right+1):
			if tree[left] < tree[mid]:
				pivot = mid
				break
		solution(left+1,pivot-1)
		solution(pivot,right)
		result.append(tree[left])

if __name__ == "__main__":
	root = 0
	while True:
		try:
			num = int(input())
			tree.append(num)
		except:
			break
	if len(tree) > 0:
		solution(0,len(tree)-1)
	for i in result:
		print(i)