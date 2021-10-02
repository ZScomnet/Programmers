import sys
input = sys.stdin.readline

def solution(K,coins):
	cnt = [100000000]*len(coins)
	money = [K]*len(coins)
	for i in range(len(coins)):
		if coins[i] <= K:
			cnt[i] = money[i] // coins[i]
			money[i] %= coins[i]
		for j in range(i+1):
			if money[j] == K:
				continue
			elif coins[i] <= money[j]:
				cnt[j] += money[j] // coins[i]
				money[j] %= coins[i] 
	answer = 100000000
	for i in range(len(coins)):
		if money[i] == 0:
			answer = min(cnt[i],answer)

	return answer
	
if __name__ == "__main__":
	N,K = map(int,input().split())
	coins = []
	for _ in range(N):
		coins.append(int(input()))
	print(solution(K,coins[::-1]))
