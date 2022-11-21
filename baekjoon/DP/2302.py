import sys
from collections import deque

input = sys.stdin.readline

def solution():
	N = int(input())
	fibo = [1,1]
	for i in range(2,41):
		fibo.append(fibo[i-2]+fibo[i-1])
	vip = []
	for i in range(int(input())):
		vip.append(int(input()))
	vip = deque(sorted(vip))
	answer = 1
	cnt = 0
	for i in range(1,N+1):
		if vip:
			if vip[0] == i:
				answer *= fibo[cnt]
				cnt = 0
				vip.popleft()
			else:
				cnt += 1
		else:
			cnt += 1
	if cnt != 0:
		answer *= fibo[cnt]
	return answer


if __name__ == "__main__":
	print(solution())