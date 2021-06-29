# 해당 알고리즘은 주어진 edge에서 싸이클을 걸러내는 알고리즘
# Tree인지 판별할 때 좋은 알고리즘
# ex) Programmers - Greedy - level3. 섬 연결하기
def is_cycle(check,node):
	if check[node] == node:
		return node
	else:
		return is_cycle(check,check[node])

def solution(node_num,edge):
	for i in edge:
		start,finish = edge[0],edge[1]
	check = [i for i in range(node_num)]
	if is_cycle(check,start) != is_cycle(check,finish): 
		# 같을 시 부모노드가 같으므로 cycle이 생김
		if check[start] < check[finish]:
			for i in range(len(check)):
				if check[i] == check[finish]:
					check[i] = check[start]
		else:
			for i in range(len(check)):
				if check[i] == check[start]:
					check[i] = check[finish]
		#check안에 수가 전부 0이 되면 tree 완성
