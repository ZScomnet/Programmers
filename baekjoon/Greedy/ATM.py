import sys
input = sys.stdin.readline

def solution(time):
	time = sorted(time)
	answer,before = 0,0
	for i in time:
		answer += before+i
		before += i
	return answer

if __name__ == "__main__":
	N = int(input())
	time = list(map(int,input().split()))
	print(solution(time))