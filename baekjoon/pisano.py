import sys
input = sys.stdin.readline

def pisano(M):
	a,b,c = 0,1,1

	for i in range(2,500000):
		a,b = b,c
		c = (a+b)%M
		if a == 0 and b == 1:
			return i-1
	if M == 2:
		return 3

	if M > 2:
		return M*M-1

if __name__ == "__main__":
	P = int(input())
	fibo = dict()
	for _ in range(P):
		N,M = map(int,input().split())
		print(N,pisano(M))
