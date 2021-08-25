import sys
sys.setrecursionlimit(10001)

def tree(node_dic,nodeinfo,node):
	if nodeinfo[0] > node[0] and node_dic[node][1] != 0:
		tree(node_dic,nodeinfo,node_dic[node][1])
	elif nodeinfo[0] < node[0] and node_dic[node][0] != 0:
		tree(node_dic,nodeinfo,node_dic[node][0])
	elif nodeinfo[0] > node[0] and node_dic[node][1] == 0:
		node_dic[node][1] = tuple(nodeinfo)
	elif nodeinfo[0] < node[0] and node_dic[node][0] == 0:
		node_dic[node][0] = tuple(nodeinfo)

def preorder(node_dic,node_num_dic,node,result):
	result.append(node_num_dic[node])
	if node_dic[node][0] != 0:
		preorder(node_dic,node_num_dic,node_dic[node][0],result)
	if node_dic[node][1] != 0:
		preorder(node_dic,node_num_dic,node_dic[node][1],result)

def postorder(node_dic,node_num_dic,node,result):
	if node_dic[node][0] != 0:
		postorder(node_dic,node_num_dic,node_dic[node][0],result)
	if node_dic[node][1] != 0:
		postorder(node_dic,node_num_dic,node_dic[node][1],result)
	result.append(node_num_dic[node])

def solution(nodeinfo):
	node_num_dic = dict()
	node_dic = dict()
	
	for node in range(len(nodeinfo)):
		node_dic[tuple(nodeinfo[node])] = [0,0]
		node_num_dic[tuple(nodeinfo[node])] = node+1

	nodeinfo = sorted(nodeinfo,key = lambda x : x[1],reverse=True)
	root = tuple(nodeinfo[0])
	for node in range(1,len(nodeinfo)):
		tree(node_dic,nodeinfo[node],root)
	pre,post = [],[]
	preorder(node_dic,node_num_dic,root,pre)
	postorder(node_dic,node_num_dic,root,post)
	return [pre,post]






	# layer = set()
	# for i in range(len(nodeinfo)):
	# 	if root[1] < nodeinfo[i][1]:
	# 		root = tuple(nodeinfo[i])
	# 	node_num_dic[tuple(nodeinfo[i])] = i+1
	# 	node_dic[tuple(nodeinfo[i])] = [0,0]
	# 	if nodeinfo[i][1] not in node_layer:
	# 		node_layer[nodeinfo[i][1]] = []
	# 	node_layer[nodeinfo[i][1]].append(tuple(nodeinfo[i]))
	# 	layer.add(nodeinfo[i][1])
	# for l in range(len(layer)-1):
	# 	for node in node_layer[layer[l]]:
	# 		length = 100001
	# 		parent_node = 0
	# 		way = ""
	# 		for parent in node_layer[layer[l+1]]:
	# 			if abs(parent[0]-node[0]) < length and node_dic[parent][1] == 0 and parent[0] < node[0]:
	# 				way = "right"
	# 				parent_node = parent
	# 				length = abs(parent[0]-node[0])
	# 			if abs(parent[0]-node[0]) < length and node_dic[parent][0] == 0 and parent[0] > node[0]:
	# 				way = "left"
	# 				parent_node = parent
	# 				length = abs(parent[0]-node[0])
	# 		if way == "left":
	# 			node_dic[parent_node][0] = node
	# 		if way == "right":
	# 			node_dic[parent_node][1] = node
	# pre,post = [],[]
	# print(node_dic)
	# preorder(node_dic,node_num_dic,root,pre)
	# postorder(node_dic,node_num_dic,root,post)

	

if __name__ == "__main__":
	print(solution([ [8,6], [3,5], [11, 5], [7,4] ]))