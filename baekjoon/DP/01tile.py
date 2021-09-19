def solution(N):
	line = [0]*1000001
	if N == 1:
		return 1
	elif N == 2:
		return 2
	else:
		line[1] = 1
		line[2] = 2
		for i in range(N-2):
			line[i+3] = line[i+1]+line[i+2]
		return line[N]

if __name__ == "__main__":
	N = int(input())
	print(solution(N))