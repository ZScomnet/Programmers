def solution(genres,plays):
	song_dic = [[] for _ in range(200000)]
	g_dic = dict()
	cnt = 0
	for g,p in zip(genres,plays):
		add = hash(g+str(p)) % 200000
		song_dic[add].append(cnt)
		cnt += 1
		try:
			g_dic[g] = g_dic[g] + [p,]
		except:
			g_dic[g] = [p,]
	for dic in g_dic.keys():
		g_dic[dic] = sorted(g_dic[dic])

	t_dic = dict()
	total_play = []
	for key,value in g_dic.items():
		t_dic[sum(value)] = key
		total_play.append(sum(value))
	total_play = sorted(total_play, reverse=True)

	result = []
	for i in total_play:
		result.append(song_dic[hash(t_dic[i]+str(g_dic[t_dic[i]][-1]))%200000][0])
		if len(g_dic[t_dic[i]]) != 1:
			del song_dic[hash(t_dic[i]+str(g_dic[t_dic[i]][-1]))%200000][0]
			result.append(song_dic[hash(t_dic[i]+str(g_dic[t_dic[i]][-2]))%200000][0])
	
	return result

print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]))