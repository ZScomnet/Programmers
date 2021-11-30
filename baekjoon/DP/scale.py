import sys
input = sys.stdin.readline

def solution(N,m,max_w,biz):
	if biz > 15000:
		return 'N'
	mg = [[0]*40001 for _ in range(31)]
	mg[0][biz] = 1
	mg[0][biz+m[0]] = 1
	mg[0][abs(biz-m[0])] = 1
	for i in range(1,N):
		mg[i][biz] = 1
		for j in range(max_w[i]+biz+i):
			if mg[i-1][j] == 1:
				mg[i][j+m[i]] = 1
				mg[i][j] = 1
				mg[i][abs(j-m[i])] = 1
	if mg[N-1][0] == 1:
		return 'Y'
	else:
		return 'N'

if __name__ == "__main__":
	N = int(input())
	m = list(map(int,input().split()))
	B = int(input())
	biz = list(map(int,input().split()))
	max_w = []
	answer = []
	for i in m:
		if len(max_w) == 0:
			max_w.append(i)
		else:
			max_w.append(max_w[-1]+i)
	for i in range(len(biz)):
		answer.append(solution(N,m,max_w,biz[i]))
	for i in answer:
		print(i,end=" ")