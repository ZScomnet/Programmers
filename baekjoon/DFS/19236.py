import sys
input = sys.stdin.readline

board = []
fish = [0]*17
fish_idx = [0]*17

d = [(0,0),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
answer = [0]

def swap(a,b,a_row,b_row,a_col,b_col):
	board[a_row][a_col],board[b_row][b_col] = board[b_row][b_col],board[a_row][a_col]
	fish_idx[a],fish_idx[b] = fish_idx[b],fish_idx[a]

def move():
	for i in range(1,len(fish)):
		for _ in range(7):
			if fish[i] > 0:
				row,col = fish_idx[i]
				if 0 <= row+d[fish[i]][0] < 4 and 0 <= col+d[fish[i]][1] < 4:
					next_row = row+d[fish[i]][0]
					next_col = col+d[fish[i]][1]
					move_point = board[next_row][next_col]
					if move_point == 0:
						board[next_row][next_col] = board[row][col]
						board[row][col] = 0
						fish_idx[i] = [next_row,next_col]
						break
					elif move_point != -1:
						swap(i,move_point,row,next_row,col,next_col)
						break	
					else:
						fish[i] += 1
						if fish[i] == 9:
							fish[i] = 1
				else:
					fish[i] += 1
					if fish[i] == 9:
						fish[i] = 1
			else:
				break

def shark(result,row,col,way):
	before_board = []
	before_fish = [0]*17
	before_idx = [0]*17
	global board
	global fish
	global fish_idx
	for i in range(4):
		line = []
		for j in range(4):
			line.append(board[i][j])
			if board[i][j] != 0:
				before_idx[board[i][j]] = [i,j]
				before_fish[board[i][j]] = fish[board[i][j]]
		before_board.append(line)
	result += board[row][col]
	way = fish[board[row][col]]
	fish[board[row][col]] = -1
	board[row][col] = -1
	move()
	for i in range(1,5):
		if 0 <= row+d[way][0]*i < 4 and 0 <= col+d[way][1]*i < 4:
			if board[row+d[way][0]*i][col+d[way][1]*i] > 0:
				board[row][col] = 0
				shark(result,row+d[way][0]*i,col+d[way][1]*i,way)
				board[row][col] = -1

	answer[0] = max(answer[0],result)
	board = before_board
	fish = before_fish
	fish_idx = before_idx
def solution():
	shark(0,0,0,0)

	return answer[0]

if __name__ == "__main__":
	for i in range(4):
		f = list(map(int,(input().split())))
		line = []
		for j in range(4):
			line.append(f[j*2])
			fish[f[j*2]] = f[j*2+1]
			fish_idx[f[j*2]] = [i,j]
		board.append(line)

	print(solution())