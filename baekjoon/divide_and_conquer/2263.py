import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

preorder = []
inorder = []
postorder = []

# def divide(inorder,postorder):
# 	if len(inorder) == 1:
# 		preorder.append(inorder[0])
# 	elif inorder and postorder:
# 		for i in range(len(inorder)):
# 			if inorder[i] == postorder[-1]:
# 				preorder.append(postorder[-1])
# 				divide(inorder[:i],postorder[:i])
# 				divide(inorder[i+1:],postorder[i:-1])

def divide(il,ir,pl,pr):
	if ir - il != pr - pl:
		return
	if il < ir and pl < pr:
		for i in range(ir-il):
			if inorder[il+i] == postorder[pr-1]:
				preorder.append(postorder[pr-1])
				divide(il,il+i,pl,pl+i)
				divide(il+i+1,ir,pl+i,pr-1)


def solution():
	divide(0,N,0,N)
	for i in preorder:
		print(i,end=" ")

if __name__ == "__main__":
	N = int(input())
	inorder = list(map(int,input().split()))
	postorder = list(map(int,input().split()))
	solution()