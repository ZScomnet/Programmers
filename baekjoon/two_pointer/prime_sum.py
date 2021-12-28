import sys
input = sys.stdin.readline

def solution(N):
	if N == 1:
		return 0

	prime = [1] * (N+1)
	for i in range(2,N+1):
		if prime[i] == 1:
			j = 2
			while (i*j) <= N:
				prime[i*j] = 0
				j += 1

	num = []
	for i in range(2,N+1):
		if prime[i]:
			num.append(i)

	left,right = 0,0
	now = num[0]
	answer = 0
	while left <= right:
		if now == N:
			answer += 1
		if now < N and right < len(num)-1:
			right += 1
			now += num[right]
		else:
			now -= num[left]
			left += 1
	return answer 

if __name__ == "__main__":
	N = int(input())
	print(solution(N))