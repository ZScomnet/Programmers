import sys
input = sys.stdin.readline

if __name__ == "__main__":
	R,C,N = map(int,input().split())
	board = []
	board_cnt = []
	for _ in range(R):
		board.append(list(input().rstrip()))
		board_cnt_line = []
		for i in board[-1]:
			if i == '.':
				board_cnt_line.append('.')
			else:
				board_cnt_line.append(0)
		board_cnt.append(board_cnt_line)
	if N == 1:
		for i in board:
			print(''.join(i))
	elif N % 2 == 0:
		for _ in range(R):
			print('O'*C)
	else:	
		dr,dc = [-1,0,1,0],[0,1,0,-1]
		for row in range(R):
			for col in range(C):
				if board_cnt[row][col] == '.':
					board_cnt[row][col] = 2
		for row in range(R):
			for col in range(C):
				if board_cnt[row][col] == 0:
					for drow,dcol in zip(dr,dc):
						if 0 <= row+drow < R and 0 <= col+dcol < C:
							if board_cnt[row+drow][col+dcol] != 0:
								board_cnt[row+drow][col+dcol] = '.'
		board_1 = []
		for row in range(R):
			board_1_line = []
			for col in range(C):
				if board_cnt[row][col] == '.' or board_cnt[row][col] == 0:
					board_1_line.append('.')
				else:
					board_1_line.append('O')
			board_1.append(board_1_line)

		for row in range(R):
			for col in range(C):
				if board_cnt[row][col] == '.':
					board_cnt[row][col] = 4
		for row in range(R):
			for col in range(C):
				if board_cnt[row][col] == 2:
					for drow,dcol in zip(dr,dc):
						if 0 <= row+drow < R and 0 <= col+dcol < C:
							if board_cnt[row+drow][col+dcol] != 2:
								board_cnt[row+drow][col+dcol] = '.'

		board_2 = []
		for row in range(R):
			board_2_line = []
			for col in range(C):
				if board_cnt[row][col] == '.' or board_cnt[row][col] == 2:
					board_2_line.append('.')
				else:
					board_2_line.append('O')
			board_2.append(board_2_line)
		while N != 3 and N != 5:
			N -= 4
		if N == 3:
			for i in board_1:
				print(''.join(i))
		else:
			for i in board_2:
				print(''.join(i))