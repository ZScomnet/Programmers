import sys
input = sys.stdin.readline

def solution(stair):
	stair = stair[::-1]
	score = [stair[0]]*len(stair)
	for now in range(len(stair)):
		if now+3 >= len(stair):
			if now == len(stair)-3:
				score[-1] = max(score[now]+stair[now+1],score[now]+stair[now+2],score[-1])
			elif now == len(stair)-2:
				score[-1] = max(score[now]+stair[now+1],score[now+1],score[-1])
		elif (now+3 < len(stair) and score[now] != score[0]) or now == 0:
			score[now+2] = max(score[now]+stair[now+2],score[now+2])
			score[now+3] = max(score[now]+stair[now+1]+stair[now+3],score[now+3])
	return score[-1]

if __name__ == "__main__":
	N = int(input())
	stair = []
	for _ in range(N):
		stair.append(int(input()))
	print(solution(stair))