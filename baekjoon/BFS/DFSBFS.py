import sys
input = sys.stdin.readline

def DFS(dic,node,result,counter):
	for i in sorted(dic[node]):
		if counter[i-1] == 0:
			result.append(i)
			counter[i-1] = 1
			DFS(dic,i,result,counter)

def BFS(dic,node,result,counter):
	depth = [node]
	while depth:
		next_depth = []
		for i in depth:
			for n in sorted(dic[i]):
				if counter[n-1] == 0:
					result.append(n)
					next_depth.append(n)
					counter[n-1] = 1
		depth = next_depth

def solution(dic,root):
	result = [root,]
	counter = [0]*len(dic)
	counter[root-1] = 1
	DFS(dic,root,result,counter)
	for i in result:
		print(i,end=" ")
	print()
	result = [root,]
	counter = [0]*len(dic)
	counter[root-1] = 1
	BFS(dic,root,result,counter)
	for i in result:
		print(i,end=" ")
	
if __name__ == "__main__":
	node,edge,root = map(int,input().split())
	dic = dict()
	for i in range(node):
		dic[i+1] = []
	for _ in range(edge):
		start,end = map(int,input().split())
		dic[start].append(end)
		dic[end].append(start)
	solution(dic,root)