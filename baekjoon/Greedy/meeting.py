import sys
input = sys.stdin.readline

def solution(meeting):
	meeting = sorted(meeting,key=lambda x:x[0])
	meeting = sorted(meeting,key=lambda x:x[1])
	answer = []
	for time in meeting:
		start,end = time
		if len(answer) == 0:
			answer.append(time)
		else:
			if answer[-1][1] <= start:
				answer.append(time)
			elif answer[-1][1]-answer[-1][0] > end-start and end < answer[-1][1]:
				answer.pop()
				answer.append(time)

	return len(answer)

if __name__ == "__main__":
	N = int(input())
	meeting = []
	for _ in range(N):
		start,end = map(int,input().split())
		meeting.append([start,end])
	print(solution(meeting))