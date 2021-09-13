def solution(info,edges):
	tree = dict()
	for i in range(len(info)):
		tree[i] = []
	for edge in edges:
		tree[edge[0]].append(edge[1])
	print(tree)
	return

if __name__ == "__main__":
	print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))