import sys
input = sys.stdin.readline

board = []
board.append([2*i for i in range(21)] + [0])
board.append([10,13,16,19,25,30,35,40,0])
board.append([20,22,24,25,30,35,40,0])
board.append([30,28,27,26,25,30,35,40,0])
log = []
for i in range(4):
	log.append([0]*len(board[i]))

def equal(unit,state):
	load, idx = unit
	if load == 0:
		if idx == 5:
			log[0][5] = log[1][0] = state
		elif idx == 10:
			log[0][10] = log[2][0] = state
		elif idx == 15:
			log[0][15] = log[3][0] = state
		elif idx == 20:
			log[0][-2] = log[1][-2] = log[2][-2] = log[3][-2] = state
		else:
			log[0][idx] = state

	elif load == 1:
		if idx == 0:
			log[0][5] = log[1][0] = state
		elif idx == 4:
			log[1][4] = log[2][3] = log[3][4] = state
		elif idx == 5:
			log[1][5] = log[2][4] = log[3][5] = state
		elif idx == 6:
			log[1][6] = log[2][5] = log[3][6] = state
		elif idx == 7:
			log[0][-2] = log[1][7] = log[2][6] = log[3][7] = state
		else:
			log[1][idx] = state

	elif load == 2:
		if idx == 0:
			log[0][10] = log[2][0] = state
		elif idx == 3:
			log[1][4] = log[2][3] = log[3][4] = state
		elif idx == 4:
			log[1][5] = log[2][4] = log[3][5] = state
		elif idx == 5:
			log[1][6] = log[2][5] = log[3][6] = state
		elif idx == 6:
			log[0][-2] = log[1][7] = log[2][6] = log[3][7] = state
		else:
			log[2][idx] = state

	elif load == 3:
		if idx == 0:
			log[0][15] = log[3][0] = state
		elif idx == 4:
			log[1][4] = log[2][3] = log[3][4] = state
		elif idx == 5:
			log[1][5] = log[2][4] = log[3][5] = state
		elif idx == 6:
			log[1][6] = log[2][5] = log[3][6] = state
		elif idx == 7:
			log[0][-2] = log[1][7] = log[2][6] = log[3][7] = state
		else:
			log[3][idx] = state

def search(dice,now,answer,units,score):
	if now == 10:
		answer[0] = max(answer[0],score)
	else:
		for i in range(4):
			load, idx = units[i]
			before = [load,idx]
			if dice[now]+idx >= len(board[load]):
				units[i][1] = len(board[load])-1
				equal(before,0)
				equal(units[i],i+1)
				search(dice,now+1,answer,units,score+board[units[i][0]][units[i][1]])
				equal(units[i],0)
				equal(before,i+1)
				units[i] = before
			elif dice[now]+idx < len(board[load]) and log[load][dice[now]+idx] == 0:
				units[i][1] += dice[now]
				equal(before,0)
				equal(units[i],i+1)
				if units[i][0] == 0 and units[i][1] == 5:
					units[i] = [1,0]
				elif units[i][0] == 0 and units[i][1] == 10:
					units[i] = [2,0]
				elif units[i][0] == 0 and units[i][1] == 15:
					units[i] = [3,0]
				search(dice,now+1,answer,units,score+board[units[i][0]][units[i][1]])
				equal(units[i],0)
				equal(before,i+1)
				units[i] = before


def solution(dice):
	answer = [0]
	units = []
	for _ in range(4):
		units.append([0,0])
	search(dice,0,answer,units,0)

	return answer[0]

if __name__ == "__main__":
	dice = list(map(int,input().split()))
	print(solution(dice))