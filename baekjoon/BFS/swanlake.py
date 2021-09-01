import sys
input = sys.stdin.readline

def print_lake(lake):
	for row in range(len(lake)):
		for col in range(len(lake[row])):
			print(lake[row][col],end="")
		print()
	print()

def swan_field(lake,start,L,search):
	drow,dcol = [-1,0,1,0],[0,1,0,-1]
	meltpoint = []
	while start:
		new_field = []
		for point in start:
			lake[point[0]][point[1]] = L
			for row,col in zip(drow,dcol):
				if 0 <= point[0]+row < len(lake) and 0 <= point[1]+col < len(lake[0]):
					if lake[point[0]+row][point[1]+col] == 0:
						lake[point[0]+row][point[1]+col] = L
						new_field.append([point[0]+row,point[1]+col])
						search[point[0]+row][point[1]+col] = 1
					elif lake[point[0]+row][point[1]+col] != 0 and lake[point[0]+row][point[1]+col] != 'X' and lake[point[0]+row][point[1]+col] != L:
						return 0
					elif lake[point[0]+row][point[1]+col] == 'X' and search[point[0]+row][point[1]+col] == 0:
						meltpoint.append([point[0]+row,point[1]+col])
						search[point[0]+row][point[1]+col] = 1
		start = new_field
	return meltpoint

def blank_field(lake,start,search):
	drow,dcol = [-1,0,1,0],[0,1,0,-1]
	meltpoint = []
	for point in start:
		for row,col in zip(drow,dcol):
			if 0 <= point[0]+row < len(lake) and 0 <= point[1]+col < len(lake[0]):
				if lake[point[0]+row][point[1]+col] == 'X':
					lake[point[0]+row][point[1]+col] = 0
					meltpoint.append([point[0]+row,point[1]+col])
	return meltpoint

if __name__ == "__main__":
	R,C = map(int,input().split())
	search = [[0]*C for _ in range(R)]
	lake = []
	start1,start2,blank = [],[],[]
	for row in range(R):
		line = input()
		lake.append(list(line)[:-1])
		for col in range(C):
			if lake[row][col] == '.':
				lake[row][col] = 0
				blank.append([row,col])
				search[row][col] = 1
			elif lake[row][col] == 'L' and len(start1) == 0:
				start1.append([row,col])
				lake[row][col] = 1
				search[row][col] = 1
			elif lake[row][col] == 'L':
				start2.append([row,col])
				lake[row][col] = 2
				search[row][col] = 1

	day = 0
	swan1 = swan_field(lake,start1,1,search)
	if swan1 == 0:
		print(0)
	else:
		start1 = swan1
	start2 = swan_field(lake,start2,2,search)
	while True:
		
		day += 1
		blank = blank_field(lake,blank,search)
		swan1 = swan_field(lake,start1,1,search)
		if swan1 == 0:
			break
		else:
			start1 = swan1
		start2 = swan_field(lake,start2,2,search)
		if start2 == 0:
			break
		print_lake(lake)
	print(day)