import sys
input = sys.stdin.readline

def solution(n):
	p0,p1 = 0,0
	if n == 0:
		p0,p1 = 1,0
	elif n == 1:
		p0,p1 = 0,1
	else:
		p0,p1 = 1,1
		for i in range(2,n):
			p0,p1 = p1,p0+p1
	return [p0,p1]

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		n = int(input())
		p0,p1 = solution(n)
		print(p0,p1)