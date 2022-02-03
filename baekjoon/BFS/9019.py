import sys
from collections import deque
input = sys.stdin.readline

def left_register(num):
	if num < 1000:
		return num*10
	else:
		return (num%1000)*10 + (num//1000)

def right_register(num):
	return (num%10) * 1000 + (num//10)

def solution(start,end):
	answer = ""
	cache = [0] * 10000
	cache[start] = 1
	q = deque([[start,""]])
	while q:
		now,stack = q.popleft()
		# D
		d = (now * 2) % 10000
		if d == end:
			answer = stack+"D"
			break
		if cache[d] == 0:
			q.append([d,stack+"D"])
			cache[d] = 1

		# S
		s = max(-9999*(now-1),now-1)
		if s == end:
			answer = stack+"S"
			break
		if cache[s] == 0:
			q.append([s,stack+"S"])
			cache[s] = 1	
		# L
		l = left_register(now)
		if l == end:
			answer = stack+"L"
			break
		if cache[l] == 0:
			q.append([l,stack+"L"])
			cache[l] = 1

		# R
		r = right_register(now)
		if r == end:
			answer = stack+"R"
			break
		if cache[r] == 0:
			q.append([r,stack+"R"])
			cache[r] = 1

	return answer

if __name__ == "__main__":
	N = int(input())
	for _ in range(N):
		start,end = map(int,input().split())
		print(solution(start,end))