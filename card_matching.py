from itertools import permutations
def search(board,permu,r,c,db,count):
	if len(permu) == 0:
		db.append(count)
		return
	board_check = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	mx,my = [0,1,0,-1],[-1,0,1,0]

	
	board_check[r][c] = 1
	if board[r][c] == permu[0]:
		count += 1
	else:
		before = count
		move_cnt = 1
		while count == before:
			for x,y in zip(mx,my):
				if 0 <= r+y < len(board) and 0 <= c+x < len(board) and [r+y,c+x] and board_check[r+y][c+x] == 0:
					board_check[r+y][c+x] = move_cnt
					if board[r+y][c+x] == permu[0]:
						count += move_cnt + 1
						r = r+y
						c = c+x
						break
				for i in range(1,4):
					if 0 <= r+y*i < len(board) and 0 <= c+x*i < len(board) and board[r+y*i][c+x*i] != 0:
						if board_check[r+y*i][c+x*i] == 0:
							board_check[r+y*i][c+x*i] = move_cnt
							if board_check[r+y*i][c+x*i] == permu[0]:
								count += move_cnt + 1
								r = r+y*i
								c = c+x*i
								break
				if count == before:
					break
			move_cnt += 1
			print(board_check)
	board_check = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	board_check[r][c] = 1
	board[r][c] = 0
	before = count
	move_cnt = 1
	while count == before:
		for x,y in zip(mx,my):
			if 0 <= r+y < len(board) and 0 <= c+x < len(board) and [r+y,c+x] and board_check[r+y][c+x]:
				board_check[r+y][c+x] = move_cnt
				if board[r+y][c+x] == permu[0]:
					count += move_cnt + 1
					r = r+y
					c = c+x
					break
			for i in range(1,4):
				if 0 <= r+y*i < len(board) and 0 <= c+x*i < len(board) and board[r+y*i][c+x*i] != 0:
					if board_check[r+y*i][c+x*i] == 0:
						board_check[r+y*i][c+x*i] = move_cnt
						if board_check[r+y*i][c+x*i] == permu[0]:
							count += move_cnt + 1
							r = r+y*i
							c = c+x*i
							break
			if count == before:
				break
		move_cnt += 1
	board[r][c] = 0
	search(board,permu[1:],r,c,db,count)





def solution(board,r,c):
	card = 0
	db = []
	for row in board:
		for col in row:
			if col > card:
				card = col
	permu_string = ""
	for i in range(1,card+1):
		permu_string += str(i)
	permu = list(permutations(permu_string,card))
	search(board,permu[1:],r,c,db,0)
	return db[0]

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))