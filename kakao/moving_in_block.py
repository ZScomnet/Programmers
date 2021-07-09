# def solution(board):
# 	board[0][0],board[0][1] = -1,-1
# 	move = [[0,0],[0,1]]
# 	cnt = -2
# 	while True:
# 		next_move = []
# 		for robot in move:
# 			try:
# 				# right
# 				if board[robot[0]][robot[1]+1] == 0:
# 					board[robot[0]][robot[1]+1] = cnt
# 					next_move.append([robot[0],robot[1]+1])
# 			except:
# 				pass
# 			try:
# 				# down
# 				if board[robot[0]+1][robot[1]] == 0:
# 					board[robot[0]+1][robot[1]] = cnt
# 					next_move.append([robot[0]+1,robot[1]])
# 			except:
# 				pass
# 			try:
# 				# left
# 				if board[robot[0]][robot[1]-1] == 0 and robot[1]-1 >= 0:
# 					board[robot[0]][robot[1]-1] = cnt
# 					next_move.append([robot[0],robot[1]-1])
# 			except:
# 				pass
# 			try:
# 				# up
# 				if board[robot[0]-1][robot[1]] == 0 and robot[0]-1 >= 0:
# 					board[robot[0]-1][robot[1]] = cnt
# 					next_move.append([robot[0]-1,robot[1]])
# 			except:
# 				pass
# 		if board[len(board)-1][len(board)-1] != 0:
# 			break
# 		cnt -= 1
# 		move = next_move
# 	for i in board:
# 		print(i)
# 	return board[len(board)-1][len(board)-1] * -1 -1

def solution(board):
	board[0][0],board[0][1] = -1,-1
	head = [[0,1]]
	tail = [[0,0]]
	cnt = -2
	while True:
		new_head = []
		new_tail = []
		print(head,tail)
		for h,t in zip(head,tail):
			#row
			if head[0] == tail[0]:
				#right
				try:
					if board[head[0]][head[1]+1] == 0 or board[tail[0]][tail[1]+1] == 0:
						new_head.append([head[0],head[1]+1])
						new_tail.append([tail[0],tail[1]+1])
						if board[head[0]][head[1]+1] == 0:
							board[head[0]][head[1]+1] = cnt
						else:
							board[tail[0]][tail[1]+1] = cnt
				except:
					pass 
				#left
				try:
					if (board[head[0]][head[1]-1] == 0 or board[tail[0]][tail[1]-1] == 0) and head[1] > 0 and tail[1] > 0:
						new_head.append([head[0],head[1]-1])
						new_tail.append([tail[0],tail[1]-1])
						if board[head[0]][head[1]-1] == 0:
							board[head[0]][head[1]-1] = cnt
						else:
							board[tail[0]][tail[1]-1] = cnt
				except:
					pass
				#clock_up
				try:
					# up spin
					if board[head[0]-1][haad[1]] != 1 and board[tail[0]-1][tail[1]] != 1 and head[0] > 0 and tail[0] > 0:
						# head
						if board[head[0]-1][head[1]] == 0:
							new_head.append([head[0],head[1]])
							new_tail.append([head[0]-1,head[1]])
						# tail
						if board[tail[0]-1][tail[1]] == 0:
							new_head.append([tail[0],tail[1]])
							new_tail.append([tail[0]-1,tail[1]])
				except:
					pass
				#clock_down
				try:
					# down spin
					if board[head[0]+1][haad[1]] != 1 and board[tail[0]+1][tail[1]] != 1:
						# head
						if board[head[0]+1][head[1]] == 0:
							new_head.append([head[0],head[1]])
							new_tail.append([head[0]+1,head[1]])
						# tail
						if board[tail[0]+1][tail[1]] == 0:
							new_head.append([tail[0],tail[1]])
							new_tail.append([tail[0]+1,tail[1]])
				except:
					pass	
			#col
			else:
				#up
				try:
					if (board[head[0]-1][head[1]] == 0 or board[tail[0]-1][tail[1]] == 0) and tail[0] > 0 and head[0] > 0:
						new_head.append([head[0]-1,head[1]])
						new_tail.append([tail[0]-1,tail[1]])
						if board[head[0]-1][head[1]] == 0:
							board[head[0]-1][head[1]] = cnt
						else:
							board[tail[0]-1][tail[1]] = cnt
				except:
					pass
				#down
				try:
					if board[head[0]+1][head[1]] == 0 or board[tail[0]+1][tail[1]] == 0:
						new_head.append([head[0]+1,head[1]])
						new_tail.append([tail[0]+1,tail[1]])
						if board[head[0]+1][head[1]] == 0:
							board[head[0]+1][head[1]] = cnt
						else:
							board[tail[0]+1][tail[1]] = cnt
				except:
					pass
				#clock_right
				try:
					if board[head[0]][head[1]+1] != 1 and board[tail[0]][tail[1]+1] != 1:
						# head
						if board[head[0]][head[1]+1] == 0:
							new_head.append([head[0],head[1]])
							new_tail.append([head[0],head[1]+1])
						# tail
						if board[tail[0]][tail[1]+1] == 0:
							new_head.append([tail[0],tail[1]])
							new_tail.append([tail[0],tail[1]+1]) 
				except:
					pass
				#clock_left
				try:
					if (board[head[0]][head[1]-1] != 1 and board[tail[0]][tail[1]-1] != 1) and head[1] > 0 and tail[1] > 0:
						# head
						if board[head[0]][head[1]-1] == 0:
							new_head.append([head[0],head[1]])
							new_tail.append([head[0],head[1]-1])
						# tail
						if board[tail[0]][tail[1]-1] == 0:
							new_head.append([tail[0],tail[1]])
							new_tail.append([tail[0],tail[1]-1])
				except:
					pass
			head = new_head
			tail = new_tail
		for i in board:
			print(i)
		if board[len(board)-1][len(board)-1] != 0:
			break
	return board[len(board)-1][len(board)-1] * -1 - 1


print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))