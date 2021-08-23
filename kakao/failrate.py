def solution(N,stages):
	now_player = len(stages)
	player = [0] * (N+2)
	dic_score = dict()
	rate = []

	for stage in stages:
		player[stage] += 1

	for stage in range(1,N+1):
		if now_player != 0:
			if player[stage] / now_player not in dic_score:
				dic_score[player[stage]/now_player] = []
			dic_score[player[stage]/now_player].append(stage)
			rate.append(player[stage]/now_player)
			now_player -= player[stage]
		else:
			if 0 not in dic_score:
				dic_score[0] = []
			dic_score[0].append(stage)
			rate.append(0)
	answer = []
	rate.sort(reverse=True)
	for i in rate:
		answer.append(dic_score[i][0])
		del dic_score[i][0]

	return answer

if __name__=="__main__":
	print(solution(10,[2]))