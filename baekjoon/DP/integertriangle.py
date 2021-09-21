def solution(triangle):
	for row in range(1,len(triangle)):
		for col in range(len(triangle[row])):
			if 0 <= col-1 < len(triangle[row-1]) and 0 <= col < len(triangle[row-1]):
				triangle[row][col] += max(triangle[row-1][col-1],triangle[row-1][col])
			elif col == 0: # left
				triangle[row][col] += triangle[row-1][col]
			else: # right
				triangle[row][col] += triangle[row-1][col-1]

	return max(triangle[-1])

if __name__ == "__main__":
	N = int(input())
	triangle = []
	for _ in range(N):
		line = list(map(int,input().split()))
		triangle.append(line)
	print(solution(triangle))