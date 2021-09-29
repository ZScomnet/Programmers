import sys
input = sys.stdin.readline

def solution(line1,line2):
	data = [[0]*1001 for _ in range(1001)]
	answer = 0
	for row in range(len(line1)-1):
		for col in range(len(line2)-1):
			if line1[row] == line2[col]:
				data[row][col] += data[row-1][col-1]+1
			else:
				data[row][col] = max(data[row][col-1],data[row-1][col])
			answer = max(answer,data[row][col])

	return answer

if __name__ == "__main__":
	line1 = input()
	line2 = input()
	print(solution(line1,line2))