import sys
input = sys.stdin.readline

answer = [-1 * 1 << 32]

def dfs(num,cal,idx):
	sums = num[0]
	for i in range(len(cal)):
		if cal[i] == -1:
			continue
		if cal[i] == '+':
			sums += num[i+1]
		elif cal[i] == '-':
			sums -= num[i+1]
		else:
			sums *= num[i+1]
	answer[0] = max(answer[0],sums)
	if idx >= len(cal):
		return
	dfs(num,cal,idx+1)
	a,b,c = num[idx],num[idx+1],cal[idx]
	if cal[idx] == '+':
		num[idx] += num[idx+1]
	elif cal[idx] == '-':
		num[idx] -= num[idx+1]
	else:
		num[idx] *= num[idx+1]
	cal[idx] = -1
	dfs(num,cal,idx+2)
	cal[idx] = c
	num[idx] = a
	num[idx+1] = b 

def solution():
	N = int(input())
	line = input().rstrip()
	num = [int(line[i]) for i in range(0,N,2)]
	cal = [line[i] for i in range(1,N,2)]
	dfs(num,cal,0)
	print(answer[0])

if __name__ == "__main__":
	solution()