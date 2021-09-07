import sys

input = sys.stdin.readline

def Fibo(n):
	a,b,c = 0,1,1
	line = [0,1,]
	for _ in range(2,1500000):
		c = (a+b)%1000000
		a,b = b,c
		line.append(c)
		if a == 0 and b == 1:
			break
	print(line[n])

if __name__ == "__main__":
	n = int(input())
	Fibo(n%1500000)