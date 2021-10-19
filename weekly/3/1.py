def solution(game_board,table):
	dx,dy = [0,1,0,-1],[-1,0,1,0]
	blocks = [0,0,[],[],[],[]]
	answer = 0
	dic = {'D' : 'L','R' : 'D','U' : 'R', 'L' : 'U'}
	s_dic = {'D' : [0,1], 'R' : [1,0], 'L' : [-1,0], 'U' : [0,-1]}
	for row in range(len(table)):
		for col in range(len(table)):
			block = []
			result = []
			if table[row][col] == 1:
				block.append([row,col])
				size = 1
				table[row][col] = -1
				while len(block) != 0:
					way = ""
					for x,y in zip(dx,dy):
						if 0 <= block[0][0] + y < len(table) and 0 <= block[0][1] + x < len(table):
							if table[block[0][0]+y][block[0][1]+x] == 1:
								block.append([block[0][0]+y,block[0][1]+x])
								size += 1
								if y == -1:
									way += 'U'
								elif x == 1:
									way += 'R'
								elif y == 1:
									way += 'D'
								elif x == -1:
									way += 'L'
								table[block[0][0]+y][block[0][1]+x] = -1
					del block[0]
					if way:
						result.append(way)
				if size <= 2:
					blocks[size-1] += 1
				else:
					blocks[size-1].append(result)
	for row in range(len(game_board)):
		for col in range(len(game_board)):
			blank = []
			result = []
			start_way = ['U']
			if game_board[row][col] == 0:
				blank.append([row,col])
				size = 1
				game_board[row][col] = -1
				while len(blank) != 0:
					way = ""
					now_way = start_way[0]
					for _ in range(4):
						if 0 <= blank[0][0] + s_dic[now_way][1] < len(game_board) and 0 <= blank[0][1] + s_dic[now_way][0] < len(game_board):
							if game_board[blank[0][0]+s_dic[now_way][1]][blank[0][1]+s_dic[now_way][0]] == 0:
								blank.append([blank[0][0]+s_dic[now_way][1],blank[0][1]+s_dic[now_way][0]])
								size += 1
								if s_dic[now_way][1] == -1:
									way += 'U'
									start_way.append('D')
								elif s_dic[now_way][0] == 1:
									way += 'R'
									start_way.append('L')
								elif s_dic[now_way][1] == 1:
									way += 'D'
									start_way.append('U')
								elif s_dic[now_way][0] == -1:
									way += 'L'
									start_way.append('R')
								game_board[blank[0][0]+s_dic[now_way][1]][blank[0][1]+s_dic[now_way][0]] = -1
						now_way = dic[now_way]
					del blank[0]
					del start_way[0]
					if way:
						result.append(way)
				if size <= 2 and blocks[size-1] != 0:
					blocks[size-1] -= 1
					answer += size
				elif 2 < size <= 6:
					valid = False
					for block in range(len(blocks[size-1])):
						for loop in range(4):
							if blocks[size-1][block] == result:
								valid = True
								break
							for way in range(len(result)):
								w = ""
								for lit in result[way]:
									w += dic[lit]
								result[way] = w
						if valid:
							del blocks[size-1][block]
							answer += size
							break
					if valid == False:
						refresh = [[row,col]]
						while len(refresh) != 0:
							game_board[row][col] = 0
							for x,y in zip(dx,dy):
								if 0 <= refresh[0][0]+y < len(game_board) and 0 <= refresh[0][1]+x < len(game_board):
									if game_board[refresh[0][0]+y][refresh[0][1]+x] == -1:
										refresh.append([refresh[0][0]+y,refresh[0][1]+x])
										game_board[refresh[0][0]+y][refresh[0][1]+x] = 0
							del refresh[0]
	return answer
print(solution([[0,0,1],[0,0,0],[1,1,1]],[[1,1,0],[1,1,0],[1,0,0]]))

# D DL
# R RD
# U UR
# L LU
