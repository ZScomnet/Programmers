import sys
input = sys.stdin.readline
from collections import deque

def droptable(point,cave,R,C):
	search = deque([[point[0],point[1]]])
	overlap = [[0]*C for _ in range(R)]
	overlap[point[0]][point[1]] = 1
	drow,dcol = [-1,0,1,0],[0,1,0,-1]
	drop = [point,]
	if point[0] == R-1:
		return
	while search:
		r,c = search.popleft()
		overlap[r][c] = 1
		for row,col in zip(drow,dcol):
			if 0 <= r+row < R and 0 <= c+col < C:
				if cave[r+row][c+col] == 'x' and overlap[r+row][c+col] == 0:
					overlap[r+row][c+col] = 1
					search.append([r+row,c+col])
					drop.append([r+row,c+col])
					if r+row == R-1:
						return
	drop_mineral(cave,drop,R,overlap)

def drop_mineral(cave,drop,R,overlap):
	fall = 101
	for point in drop:
		for i in range(point[0]+1,R):
			if overlap[i][point[1]] == 1:
				break
			if cave[i][point[1]] == 'x':
				if fall > i-1-point[0]:
					fall = i-1-point[0]
					break
				else:
					break
			elif i == R-1 and fall > i-point[0]:
				fall = i-point[0]
	if fall != 101:
		for point in drop:
			cave[point[0]][point[1]] = '.'
		for point in drop:
			cave[point[0]+fall][point[1]] = 'x'
	

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
	for row in cave:
		print(''.join(row),end="")
	print()