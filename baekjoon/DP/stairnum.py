import sys
input = sys.stdin.readline

def solution(N):
	memory = [[0,1,1,1,1,1,1,1,1,1]] + [[0]*10 for _ in range(N-1)]
	for row in range(1,N):
		for col in range(10):
			if col == 0:
				memory[row][col] = memory[row-1][1] % 1000000000
			elif 1 <= col <= 8:
				memory[row][col] = (memory[row-1][col-1] + memory[row-1][col+1]) % 1000000000
			else:
				memory[row][col] = memory[row-1][8] % 1000000000	

	return sum(memory[N-1]) % 1000000000

if __name__ == "__main__":
	N = int(input())
	print(solution(N))