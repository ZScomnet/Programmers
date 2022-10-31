import sys
input = sys.stdin.readline

def solution():
	N = int(input())
	answer = 0
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))

	gift = [[b[i],a[i]] for i in range(N)]
	gift = sorted(gift)
	max_date = 0
	limit = 0
	before = -1
	for i in range(N):
		bi,ai = gift[i]
		if ai < bi:
			if (bi-ai) % 30 != 0:
				answer += (bi-ai) // 30 + 1
				ai += 30 * ((bi-ai) // 30 + 1)
			else:
				answer += (bi-ai) // 30
				ai += 30 * ((bi-ai) // 30)
		max_date = max(max_date,ai)
		if before != bi:
			limit = max_date
			max_date = 0
			before = bi
		if ai < limit:
			if (limit-ai) % 30 != 0:
				answer += (limit-ai) // 30 + 1
				ai += 30 * ((limit-ai) // 30 + 1)
			else:
				answer += (limit-ai) // 30
				ai += 30 * ((limit-ai) // 30)
		max_date = max(max_date,ai)

	return answer

if __name__ == "__main__":
	print(solution())