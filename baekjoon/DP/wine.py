import sys
input = sys.stdin.readline

def solution(wine):
	line = [0] * len(wine)
	for i in range(len(wine)):
		if line[i] == 0:
			line[i] = wine[i]
		if i+3 < len(wine):
			line[i+3] = max(line[i]+wine[i+1]+wine[i+3],line[i+3])
			line[i+2] = max(line[i]+wine[i+2],line[i+2],line[i]+wine[i+1])
		else:
			if i == len(wine)-3:
				line[-1] = max(line[i]+wine[i+1],line[i]+wine[i+2])
			elif i == len(wine)-2:
				line[-1] = max(line[i]+wine[-1],line[i+1])
			else:
				line[-1] = line[i]

	return line[-1]

if __name__ == "__main__":
	N = int(input())
	wine = []
	for _ in range(N):
		wine.append(int(input()))
	print(solution(wine))