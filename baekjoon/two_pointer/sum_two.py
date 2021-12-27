import sys
input = sys.stdin.readline

def solution(num,result):
	left,right = 0,len(num)-1
	answer = 0
	num = sorted(num)
	while left < right:
		if num[left] + num[right] == result:
			answer += 1
		if num[left] + num[right] > result:
			right -= 1
		else:
			left += 1

	return answer

if __name__ == "__main__":
	n = int(input())
	num = list(map(int,input().split()))
	result = int(input())
	print(solution(num,result))