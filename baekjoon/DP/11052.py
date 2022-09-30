def solution():
	N = int(input())
	P = list(map(int,input().split()))
	for i in range(len(P)):
		for j in range(i):
			P[i] = max(P[i],P[i-1-j]+P[j])
	print(P[-1])
if __name__ == "__main__":
	solution()