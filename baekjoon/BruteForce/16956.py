import sys
input = sys.stdin.readline

def solution():
	R,C = map(int,input().split())
	farm = []
	for i in range(R):
		farm.append(list(input().rstrip()))
	for row in range(R):
		for col in range(C):
			if farm[row][col] == 'S':
				for drow,dcol in zip([-1,0,1,0],[0,1,0,-1]):
					if 0 <= row+drow < R and 0 <= col+dcol < C:
						if farm[row+drow][col+dcol] == '.':
							farm[row+drow][col+dcol] = 'D'
						elif farm[row+drow][col+dcol] == 'W':
							print(0)
							return
	print(1)
	for i in range(R):
		print(''.join(farm[i]))

if __name__ == "__main__":
	solution()