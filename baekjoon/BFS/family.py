import sys

input = sys.stdin.readline

def search(family,depth,now,b,N):
	answer = 0
	if now == b:
		return depth
	for i in range(1,N+1):
		if family[now][i] == 1 and now != i:
			family[now][i] = 0
			family[i][now] = 0
			answer += search(family,depth+1,i,b,N)
			if answer != 0:
				break
	if answer != 0:
		return answer
	else:
		return 0

def solution(family,a,b,N):
	answer = search(family,0,a,b,N)
	if answer == 0:
		return -1
	else:
		return answer

if __name__ == "__main__":
	N = int(input())
	family = [[0] * 101 for _ in range(101)]
	a,b = map(int,input().split())
	T = int(input())
	for _ in range(T):
		child,parent = map(int,input().split())
		family[child][parent] = 1
		family[parent][child] = 1
	print(solution(family,a,b,N))