import sys
from collections import deque
input = sys.stdin.readline

def BFS(start,jail):
	drow,dcol = [-1,0,1,0],[0,1,0,-1]
	check = [[-1]*len(jail[0]) for _ in range(len(jail))]
	q = deque([tuple(start)])
	check[start[0]][start[1]] = 0
	while q:
		row,col = q.popleft()
		for r,c in zip(drow,dcol):
			if 0 <= row+r < len(check) and 0 <= col+c < len(check[0]):
				if check[row+r][col+c] >= 0:
					continue
				if jail[row+r][col+c] == '#':
					check[row+r][col+c] = check[row][col]+1
					q.append((row+r,col+c))
				elif jail[row+r][col+c] == '.':
					check[row+r][col+c] = check[row][col]
					q.appendleft((row+r,col+c))

	return check
if __name__ == "__main__":
	N = int(input())
	for _ in range(N):
		jail = []
		a,b = 0,0
		h,w = map(int,input().split())
		jail.append(['.']*(w+2))
		for _ in range(h):
			jail.append(['.']+ list(input())[:-1] + ['.'])
		jail.append(['.']*(w+2))
		for row in range(len(jail)):
			for col in range(len(jail[row])):
				if jail[row][col] == '$' and a == 0:
					a = [row,col]
					jail[row][col] = '.'
				elif jail[row][col] == '$' and b == 0:
					b = [row,col]
					jail[row][col] = '.'
		amap = BFS(a,jail)
		bmap = BFS(b,jail)
		cmap = BFS([0,0],jail)
		answer = -1
		for row in range(h+2):
			for col in range(w+2):
				if jail[row][col] == '*' or amap[row][col] < 0 or bmap[row][col] < 0 or cmap[row][col] < 0:
					continue
				opencnt = amap[row][col] + bmap[row][col] + cmap[row][col]
				if jail[row][col] == '#':
					opencnt-=2
				if answer == -1 or answer > opencnt:
					print((row,col),amap[row][col],bmap[row][col],cmap[row][col])
					answer = opencnt
		print(answer)