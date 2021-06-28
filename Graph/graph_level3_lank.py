def solution(n,results):
	win = [set() for _ in range(n)]
	lose = [set() for _ in range(n)]
	result = 0
	for i in results:
		win[i[0]-1].update([i[1]])
		lose[i[1]-1].update([i[0]])
	for player in range(n):
		for i in win[player]:
			win[player] = win[player] | win[i-1]
	for player in range(n):
		for i in lose[player]:
			lose[player] = lose[player] | lose[i-1]

	for player in range(n):
		for i in win[player]:
			win[player] = win[player] | win[i-1]
	for player in range(n):
		for i in lose[player]:
			lose[player] = lose[player] | lose[i-1]

	for i in range(n):
		if len(win[i]) + len(lose[i]) == n-1:
			result += 1

	return result

print(solution(5,[[2,1],[2,3],[2,4],[2,5]]))