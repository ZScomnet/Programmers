import sys
input = sys.stdin.readline

def solution(matrixes):
	dp = [[0]*len(matrixes) for _ in range(len(matrixes))]
	s = [[0]*len(matrixes) for _ in range(len(matrixes))]
	for i in range(len(matrixes)):
		s[i][i] = (matrixes[i][0],matrixes[i][1])
	for depth in range(1,len(matrixes)):
		for row in range(len(matrixes)-depth):
			for start in range(depth):
				if dp[row][row+depth] == 0:
					dp[row][row+depth] = s[row][row+start][0] * s[row][row+start][1] * s[row+1][row+depth][1] + dp[row][row+start] + dp[row+1][row+depth]
					s[row][row+depth] = (s[row][row+start][0],s[row+1][row+depth][1])
				else:
					dp[row][row+depth] = min(dp[row][row+depth],s[row][row+start][0] * s[row][row+start][1] * s[row+start+1][row+depth][1] + dp[row][row+start]+dp[row+start+1][row+depth])
	return dp[0][-1]

if __name__ == "__main__":
	N = int(input())
	matrixes = []
	for _ in range(N):
		matrixes.append(list(map(int,input().split())))
	print(solution(matrixes))