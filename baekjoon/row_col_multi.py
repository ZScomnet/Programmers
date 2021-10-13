import sys

input = sys.stdin.readline

def solution(a,b):
	result = [[0]*len(b) for _ in range(len(a))]
	for a_row in range(len(a)):
		for b_row in range(len(b)):
			for idx in range(len(a[a_row])):
				result[a_row][b_row] += a[a_row][idx] * b[b_row][idx]

	for row in range(len(result)):
		for col in range(len(result[row])):
			print(result[row][col],end=" ")
		print()

if __name__ == "__main__":
	N,M = map(int,input().split())
	a = []
	for _ in range(N):
		a.append(list(map(int,input().split())))
	N,M = map(int,input().split())
	b_before = []
	for _ in range(N):
		b_before.append(list(map(int,input().split())))
	b = []
	for col in range(len(b_before[0])):
		line = []
		for row in range(len(b_before)):
			line.append(b_before[row][col])
		b.append(line)
	solution(a,b)