def solution(places):

	sy,sx = [-1,0,1,0],[0,1,0,-1]
	dy,dx = [-2,-1,0,1,2,1,0,-1],[0,1,2,1,0,-1,-2,-1]
	result = []
	for place in places:
		is_safe = 1 # 안전한 곳인가? 판별
		for row in range(0,5): # 행
			for col in range(0,5): # 렬
				safe_zone = [0,0,0,0,0,0,0,0] # 거리 2 안전한가?
				zone = [0,2,4,6]
				if place[row][col] == 'P': # 대기자면 수행
					for y,x,z in zip(sy,sx,zone): # 거리 1 탐색 / safe_zone 탐색
						if 0 <= row+y < 5 and 0 <= col+x < 5:
							if place[row+y][col+x] == 'P': # 사람있으면 그냥 탈락
								is_safe = 0
							elif place[row+y][col+x] == 'X': # 벽이면 safe_zone 갱신
								safe_zone[z] = 1
					for i in [1,3,5]: # 대각선 구간 안전한지 판단
						if safe_zone[i-1] == 1 and safe_zone[i+1] == 1:
							safe_zone[i] = 1
					if safe_zone[0] == 1 and safe_zone[6] == 1:
						safe_zone[7] = 1
					if is_safe == 0:
						break
					for y,x,safe in zip(dy,dx,safe_zone): # 거리2 탐색
						if 0 <= row+y < 5 and 0 <= col+x <5:
							if place[row+y][col+x] == 'P' and safe == 0:
								is_safe = 0
						if is_safe == 0:
							break		
				
			if is_safe == 0:
				break
		result.append(is_safe)

	return result

print(solution([["PXPXP", "XPXPX", "PXPXP", "OOOOO", "PXXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))