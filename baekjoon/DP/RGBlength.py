import sys
input = sys.stdin.readline

def solution(colors):
	for i in range(1,len(colors)):
		colors[i][0] += min(colors[i-1][1],colors[i-1][2])
		colors[i][1] += min(colors[i-1][0],colors[i-1][2])
		colors[i][2] += min(colors[i-1][0],colors[i-1][1])
	return min(colors[-1])
if __name__ == "__main__":
	N = int(input())
	colors = []
	for _ in range(N):
		line = list(map(int,input().split()))
		colors.append(line)
	print(solution(colors))