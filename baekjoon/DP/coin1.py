import sys
input = sys.stdin.readline

def solution(n,k,coins):
	answer = 0
	before = [0]*(k+1)
	before[0] = 1
	for i in range(n):
		now = [0] * (k+1)
		now[0] = 1
		for j in range(k+1):
			if j >= coins[i]:
				now[j] = before[j] + now[j-coins[i]]
			else:
				now[j] = before[j]
		before = now
	return now[-1]

if __name__ == "__main__":
	n,k = map(int,input().split())
	coins = []
	for _ in range(n):
		coins.append(int(input()))
	print(solution(n,k,coins))