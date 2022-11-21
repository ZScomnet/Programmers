import sys
input = sys.stdin.readline

def solution():
	T = int(input())
	for t in range(T):
		N = int(input())
		h = list(map(int,input().split()))
		if N == 1:
			print("YES")
		else:
			answer = "YES"
			down = 1
			for i in range(1,N):
				if h[i-1] > h[i] and down == 0:
					answer = "NO"
					break
				elif h[i-1] < h[i] and down == 1:
					down = 0
			print(answer)

if __name__ == "__main__":
	solution()
