from collections import deque
import sys
input = sys.stdin.readline

answer = []

def solution():
	N = int(input())
	tank = []
	board = [[0]*N for _ in range(N)]
	for i in range(N):
		tank.append(list(map(int,input().split())))	
		row,col = tank[-1]
		board[row][col] = i+1
	

	return

if __name__ == "__main__":
	solution()