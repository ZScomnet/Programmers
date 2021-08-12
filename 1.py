def solution(n,build_frame):
	n += 1
	pillar_check = [[0]*n] + [[-1]*(n)]*(n-1)
	board_check = [[-1]*n]*n
	n -= 1
	# -1 설치 불가능 0 설치 가능 1 설치 상태
	for build in build_frame:
		x,y,a,b = build[0],build[1],build[2],build[3]
		if a == 0:
			if b == 0:
				if board_check[y+1][x] == 1 and board_check[y+1][x-1] != 1 and board_check[y+1][x+1] != 1:
					continue
				elif board_check[y+1][x-1] == 1 and board_check[y+1][x] != 1 and board_check[y+1][x-2] != 1:
					continue
				elif pillar_check[y+1][x] == 1:
					if x == 0:
						if board_check[y+1][x] != 1:
							continue
					elif x == n:
						if board_check[y+1][x-1] != 1:
							continue
					else:
						if board_check[y+1][x] != 1 or board_check[y+1][x-1] != 1:
							continue
				pillar_check[y][x] = 0
			else:
				if pillar_check[y][x] == 0:
					pillar_check[y][x] = 1
					if y < n-1:
						if pillar_check[y+1][x] == -1:
							# pillar_check[y][x] = 0
							print("pass")
						print(x,y,a,b)
						print(pillar_check)
					if y < n:
						if board_check[y+1][x] == -1:
							board_check[y+1][x] = 0
						print(x,y,a,b)
						print(pillar_check)
					if x > 0 and board_check[y+1][x-1] == -1:
						board_check[y+1][x-1] = 0

		else:
			if b == 0:
				if x < n:
					if pillar_check[y][x+1] == 1 and pillar_check[y-1][x+1] != 1 and board_check[y][x+1] != 1:
						continue
				if x > 0:
					if pillar_check[y][x] == 1 and pillar_check[y-1][x] != 1 and board_check[y][x-1] != 1:
						continue
				if x < n-1:
					if board_check[y][x+1] == 1 and pillar_check[y-1][x+1] != 1 and pillar_check[y-1][x+2] != 1:
						continue
				if x > 0:
					if board_check[y][x-1] == 1 and pillar_check[y-1][x-1] != 1 and pillar_check[y-1][x] != 1:
						continue
				board_check[y][x] = 0

			else:
				if board_check[y][x] == 0 and x < n:
					board_check[y][x] = 1
					if pillar_check[y][x+1] == -1:
						pillar_check[y][x+1] == 0
					if pillar_check[y][x] == -1:
						pillar_check[y][x] == 0
					if x+2 < n:
						if board_check[y][x] == 1 and board_check[y][x+2] == 1 and board_check[y][x+1] == -1:
							board_check[y][x+1] = 0

		print("-------------------------")
	result = []
	for row in range(n+1):
		for col in range(n+1):
			if pillar_check[row][col] == 1:
				result.append([col,row,0])
			if board_check[row][col] == 1:
				result.append([col,row,1])

	return result

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))