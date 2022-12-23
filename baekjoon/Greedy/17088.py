import sys
input = sys.stdin.readline

def check(arr,count):
	answer = 1e9
	isNumArray = True
	nextArr = [arr[i] for i in range(len(arr))]
	cnt = count
	g = arr[1]-arr[0]
	for i in range(1,len(arr)):
		if nextArr[i]-nextArr[i-1] == g:
			continue
		elif nextArr[i]-nextArr[i-1] == g-1:
			nextArr[i] += 1
			cnt += 1
		elif nextArr[i]-nextArr[i-1] == g+1:
			nextArr[i] -= 1
			cnt += 1
		else:
			isNumArray = False
			break
	if isNumArray:
		answer = min(answer,cnt)
	return answer

def solution():
	N = int(input())
	arr = list(map(int,input().split()))
	answer = 1e9
	if len(arr) == 1:
		print(0)
		return
	for i,j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
		count = abs(i) + abs(j)
		arr[0] += i
		arr[1] += j
		answer = min(answer,check(arr,count))
		arr[0] -= i
		arr[1] -= j
	if answer == 1e9:
		print(-1)
	else:
		print(answer)

if __name__ == "__main__":
	solution()