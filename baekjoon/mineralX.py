import sys
input = sys.stdin.readline

def droptable(point,cave,R,C):
	search = [point,]
	overlap = [[0]*C for _ in range(R)]
	overlap[point[0]][point[1]] = 1
	drow,dcol = [-1,0,1,0],[0,1,0,-1]
	drop = []
	dic = dict()
	dic[point[1]] = point[0]
	while len(search) != 0:
		new_search = []
		for p in search:
			overlap[p[0]][p[1]] = 1
			for row,col in zip(drow,dcol):
				if 0 <= p[0]+row < R and 0 <= p[1]+col < C:
					if cave[p[0]+row][p[1]+col] == 'x' and overlap[p[0]+row][p[1]+col] == 0:
						new_search.append([p[0]+row,p[1]+col])
						if p[0]+row == R-1:
							return
						if p[1]+col not in dic:
							dic[p[1]+col] = p[0]+row
						elif dic[p[1]+col] < p[0]+row:
							dic[p[1]+col] = p[0]+row
		drop += search
		search = new_search
	depth = R
	for col,row in zip(dic.keys(),dic.values()):
		for i in range(row+1,R):
			if cave[i][col] == 'x' and i-row < depth:
				depth = i-row-1
				break
			if i == R-1 and cave[i][col] == '.' and i-row < depth:
				depth = i-row
	for d in drop:
		cave[d[0]][d[1]] = '.'
	for d in drop:
		cave[d[0]+depth][d[1]] = 'x'

def print_cave(cave):
	for row in cave:
		for col in row:
			print(col,end="")

if __name__=="__main__":
	R,C = map(int,input().split())
	cave = []
	for _ in range(R):
		line = list(input())
		cave.append(line)

	N = int(input())
	shot = list(map(int,input().split()))
	left = True
	for i in shot:
		if left:
			for col in range(C):
				if cave[R-i][col] == 'x':
					cave[R-i][col] = '.'
					if 0 <= col+1 < C:
						if cave[R-i][col+1] == 'x':
							droptable([R-i,col+1],cave,R,C) 
					if 0 <= R-i-1 < R:
						if cave[R-i-1][col] == 'x':
							droptable([R-i-1,col],cave,R,C)
					break
			left = False
		else:
			for col in range(C-1,-1,-1):
				if cave[R-i][col] == 'x':
					cave[R-i][col] = '.'
					if 0 <= col-1 < C:
						if cave[R-i][col-1] == 'x':
							droptable([R-i,col-1],cave,R,C) 
					if 0 <= R-i-1 < R:
						if cave[R-i-1][col] == 'x':
							droptable([R-i-1,col],cave,R,C)
					break
			left = True
	print_cave(cave)