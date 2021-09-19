import sys
input = sys.stdin.readline

def solution(N):
	num = [1,1,1,2,2,3,4,5,7,9,12]
	if N <= 10:
		return num[N-1]
	else:
		n1,n2,n3,n4 = 5,7,9,12
		for _ in range(11,N):
			n1,n2,n3,n4 = n2,n3,n4,n2+n3
		return n4
if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		N = int(input())
		print(solution(N))