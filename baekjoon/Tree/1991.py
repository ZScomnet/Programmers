# import sys
# input = sys.stdin.readline

# def preorder(tree,now):
# 	if now == ".":
# 		return ""
# 	else:
# 		return now + preorder(tree,tree[now][0]) + preorder(tree,tree[now][1])

# def inorder(tree,now):
# 	if now == ".":
# 		return ""
# 	else:
# 		return inorder(tree,tree[now][0]) + now + inorder(tree,tree[now][1])

# def postorder(tree,now):
# 	if now == ".":
# 		return ""
# 	else:
# 		return postorder(tree,tree[now][0]) + postorder(tree,tree[now][1]) + now

# def solution(tree):
# 	print(preorder(tree,"A"))
# 	print(inorder(tree,"A"))
# 	print(postorder(tree,"A"))

# if __name__ == "__main__":
# 	N = int(input())
# 	tree = dict()
# 	for i in range(N):
# 		tree[chr(ord('A')+i)] = []

# 	for _ in range(N):
# 		parent,left,right = input().split()
# 		tree[parent].append(left)
# 		tree[parent].append(right)
# 	solution(tree)

import sys
input = sys.stdin.readline

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None

	def preorder(self,now):
		if now == None:
			return ""
		else:
			return now.data + self.preorder(now.left) + self.preorder(now.right)

	def inorder(self,now):
		if now == None:
			return ""
		else:
			return self.inorder(now.left) + now.data + self.inorder(now.right)

	def postorder(self,now):
		if now == None:
			return ""
		else:
			return self.postorder(now.left) + self.postorder(now.right) + now.data


def solution(tree):
	print(tree.preorder(tree.root))
	print(tree.inorder(tree.root))
	print(tree.postorder(tree.root))

if __name__ == "__main__":
	N = int(input())
	node_dic = dict()
	for i in range(N):
		node_dic[chr(ord('A')+i)] = Node(chr(ord('A')+i))
	tree = Tree()
	tree.root = node_dic['A']
	for _ in range(N):
		parent,left,right = input().split()
		if left != '.':
			node_dic[parent].left = node_dic[left]
		if right != '.':
			node_dic[parent].right = node_dic[right]
	solution(tree)












