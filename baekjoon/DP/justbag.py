def solution(N,K,things):
	memorization = [[0] * (K+1) for _ in range(N+1)]
	for row in range(1,N+1):
		thing = things[row-1]
		for col in range(1,K+1):
			if row == 1 and col >= thing[0]:
				memorization[row][col] = thing[1]
			else:
				if col < thing[0]:
					memorization[row][col] = max(memorization[row][col-1],memorization[row-1][col])
				else:
					memorization[row][col] = max(memorization[row-1][col],memorization[row-1][col-thing[0]]+thing[1])
	return memorization[N][K]

if __name__ == "__main__":
	N,K = map(int,input().split())
	things = []
	for _ in range(N):
		thing = tuple(map(int,input().split()))
		things.append(thing)
	print(solution(N,K,things))