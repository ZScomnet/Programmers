def solution(n,info):
	score = [10,9,8,7,6,5,4,3,2,1,0]
	answer = [-1]
	gap = 0
	for i in range(11):
		point = n
		board = [0,0,0,0,0,0,0,0,0,0,0]
		for r in range(i,11):
			if point == 0:
				break
			if point > info[r]:
				board[r] = info[r] + 1
				point -= info[r] + 1
		apeach,ryan = 0,0
		for r in range(11):
			if info[r] < board[r]:
				ryan += score[r]
			elif info[r] >= board[r] and info[r] != 0:
				apeach += score[r]
		if gap < ryan-apeach:
			gap = ryan-apeach
			answer = board
	if gap == 0:
		return answer
	drop_score = []
	while len(drop_score) != 11:
		board = answer.copy()
		point = n
		index,size = 0,0
		for i in range(11):
			if size <= board[i] and i not in drop_score:
				size = board[i]
				index = i
			point -= board[i]
		board[index] = 0
		drop_score.append(index)
		point += size
		for i in range(index+1,11):
			if i not in drop_score and board[i] == 0 and point > info[i]:
				board[i] = info[i]+1
				point -= info[i]+1
		apeach,ryan = 0,0
		for r in range(11):
			if info[r] < board[r]:
				ryan += score[r]
			elif info[r] >= board[r] and info[r] != 0:
				apeach += score[r]
		if gap < ryan-apeach:
			gap = ryan-apeach
			answer = board
		elif gap == ryan-apeach:
			for r in range(10,-1,-1):
				if answer[r] > board[r]:
					break
				elif answer[r] < board[r]:
					answer = board
					break
	if sum(answer) != n:
		answer[-1] += n-sum(answer)

	return answer

if __name__ == "__main__":
	print(solution(5,[1,0,0,1,0,0,0,0,0,0,3]))