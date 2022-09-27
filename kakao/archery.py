answer = [-1]
max_gap = [-1]
def dfs(n,info,score,my_info,my_score,depth):
	if depth == 10:
		if n != 0:
			my_info[depth] = n
		if max_gap[0] < my_score-score and my_score-score > 0:
			answer[0] = my_info.copy()
			max_gap[0] = my_score-score
		elif max_gap[0] == my_score-score and my_score-score > 0:
			for i in range(11):
				if answer[0][depth-i] > my_info[depth-i]:
					return
				elif answer[0][depth-i] < my_info[depth-i]:
					answer[0] = my_info.copy()
					max_gap[0] = my_score-score
					break

		if n != 0:
			my_info[depth] = 0
		return

	if info[depth] < n:
		my_info[depth] = info[depth]+1
		if info[depth] != 0:
			dfs(n-info[depth]-1,info,score-(10-depth),my_info,my_score+(10-depth),depth+1)	
		else:
			dfs(n-1,info,score,my_info,my_score+(10-depth),depth+1)
		my_info[depth] = 0
	dfs(n,info,score,my_info,my_score,depth+1)

def solution(n, info):
	score = 0
	for i in range(11):
		if info[i] != 0:
			score += 10-i
	dfs(n,info,score,[0,0,0,0,0,0,0,0,0,0,0],0,0)
	if answer[0] == -1:
		return [-1]
	return answer[0]

if __name__ == "__main__":
	print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))