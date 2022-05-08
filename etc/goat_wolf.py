answer = [0]

def search(tree,cnt_tree,now,info,goat,wolf):
	save = -1
	save_cnt_goat = cnt_tree[now][0]
	save_cnt_wolf = cnt_tree[now][1]

	if info[now] == 0:
		goat += 1
		info[now] = -1
		save = 0
	elif info[now] == 1:
		wolf += 1
		info[now] = -1
		save = 1

	if goat <= wolf:
		info[now] = save
		return

	answer[0] = max(answer[0],goat)
	cnt_tree[now][0] = goat
	cnt_tree[now][1] = wolf
	for n in tree[now]:
		if cnt_tree[now] != cnt_tree[n]:
			search(tree,cnt_tree,n,info,goat,wolf)
			
	cnt_tree[now][0] = save_cnt_goat
	cnt_tree[now][1] = save_cnt_wolf
	info[now] = save

def solution(info,edges):
	tree = dict()
	cnt_tree = dict()
	counter = [0] * len(info)
	for i in range(len(info)):
		tree[i] = []
		cnt_tree[i] = [0,0]
	
	for edge in edges:
		start,end = edge
		tree[start].append(end)
		tree[end].append(start)

	search(tree,cnt_tree,0,info,0,0)

	return answer[0]


if __name__ == "__main__":
	print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))