def DFS(words,target,begin,db,change):
	if target == begin:
		db.append(sum(change))
	for i in range(len(change)):
		if change[i] == 0:
			diff = 0
			for b,t in zip(begin,words[i]):
				if b != t:
					diff +=1

			if diff == 1:
				change[i] = 1
				DFS(words,target,words[i],db,change)
				change[i] = 0

def solution(begin,target,words):
	if target not in words:
		return 0
	db = []
	change = [0 for _ in range(len(words))]
	DFS(words,target,begin,db,change)
	return min(db)

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))