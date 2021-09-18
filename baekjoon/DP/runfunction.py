import sys
input = sys.stdin.readline

def divide(a,b,c,memory):
	if a <= 0 or b <= 0 or c <= 0:
		return 1
	else:
		if a > 20 or b > 20 or c > 20:
			memory[20][20][20] = divide(20,20,20,memory)
			return memory[20][20][20]
		elif memory[a][b][c] != -1:
			return memory[a][b][c]
		elif a < b and b < c and memory[a][b][c] == -1:
			memory[a][b][c] = divide(a,b,c-1,memory) + divide(a,b-1,c-1,memory) - divide(a,b-1,c,memory)
		elif memory[a][b][c] == -1:
			memory[a][b][c] = divide(a-1,b,c,memory) + divide(a-1,b-1,c,memory) + divide(a-1,b,c-1,memory) - divide(a-1,b-1,c-1,memory)
		return memory[a][b][c]		
def solution(a,b,c):
	answer = 0
	memory = [[[-1]*21 for _ in range(21)] for _ in range(21)]
	answer += divide(a,b,c,memory)
	return answer

if __name__ == "__main__":
	while True:
		a,b,c = list(map(int,input().split()))
		if a == b == c == -1:
			break
		print("w("+str(a)+", "+str(b)+", "+str(c)+") =",solution(a,b,c))