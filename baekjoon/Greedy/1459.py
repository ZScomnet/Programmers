import sys
input = sys.stdin.readline

def solution():
	X,Y,W,S = map(int,input().split())
	answer = 0
	if W*2 < S:
		answer += min(X,Y) * W*2
	else:
		answer += min(X,Y) * S
	X,Y = X-min(X,Y),Y-min(X,Y)
	length = max(X,Y)
	if length % 2 != 0:
		length -= 1
		answer += W
	if S < W:
		answer += length * S
	else:
		answer += length * W
	return answer

if __name__ == "__main__":
	print(solution())