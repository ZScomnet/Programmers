def solution(board):
	head = [[0,1]]
	tail = [[0,0]]
	board[0][0],board[0][1] = -1,-1 
	movex,movey = [0,1,0,-1],[-1,0,1,0]
	n = len(board)
	cnt = -2
	while board[n-1][n-1] == 0:
		new_head = []
		new_tail = []
		for h,t in zip(head,tail):
			#move
			for y,x in zip(movey,movex): # move up->right->down->left
				if 0 <= x+h[1] < n and 0 <= y+h[y] < n and 0 <= x+t[1] < n and 0 <= y+t[0] < n:
					if board[y+h[0]][x+h[1]] == 0 or board[y+t[0]][x+t[1]] == 0:
						new_head.append([y+h[0],x+h[1]])
						new_tail.append([y+t[0],x+t[1]])
						board[y+h[0]][x+h[1]] = cnt
						board[y+t[0]][x+t[1]] = cnt
			#spin_row
			if h[0] == t[0]:
				#spin_down
				if 0 <= h[0]+1 < n and 0 <= t[0]+1 < n and board[h[0]+1][h[1]] != 1 and board[t[0]+1][t[1]] != 1:
					new_head.append([h[0],h[1]])
					new_tail.append([h[0]+1,h[1]])
					new_head.append([t[0],t[1]])
					new_tail.append([t[0]+1,t[1]])
				#spin_up

				if 0 <= h[0]-1 < n and 0 <= t[0]-1 < n and board[h[0]-1][h[1]] != 1 and board[t[0]-1][t[1]] != 1:
					print(h,t)
					new_head.append([h[0],h[1]])
					new_tail.append([h[0]-1,h[1]])
					new_head.append([t[0],t[1]])
					new_tail.append([t[0]-1,t[1]])
				print(new_head)
				print(new_tail)
			#spin_col
			else:
				#spin_right
				if (0 <= h[1]+1 < n and 0 <= t[1]+1 < n) and board[h[0]][h[1]+1] != 1 and board[t[0]][t[1]+1] != 1:
					new_head.append([h[0],h[1]])
					new_tail.append([h[0],h[1]+1])
					new_head.append([t[0],t[1]])
					new_tail.append([t[0],t[1]+1])
				#spin_left
				if (0 <= h[1]-1 < n and 0 <= t[1]-1 < n) and board[h[0]][h[1]-1] != 1 and board[t[0]][t[1]-1] != 1:
					new_head.append([h[0],h[1]])
					new_tail.append([h[0],h[1]-1])
					new_head.append([t[0],t[1]])
					new_tail.append([t[0],t[1]-1])
		for i in board:
			print(i)
		print("-------------")
		cnt -= 1
		head = new_head
		tail = new_tail

	return board[n-1][n-1]*-1 -1

print(solution([[0, 0, 0, 0, 0, 0, 0], [0,0,0,0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]))