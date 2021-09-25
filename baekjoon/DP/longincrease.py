import sys
input = sys.stdin.readline

def solution(line):
	cnt = [1] * len(line)
	for right in range(len(line)):
		for left in range(right):
			if line[right] > line[left]:
				cnt[right] = max(cnt[right],cnt[left]+1)

	return max(cnt)

if __name__ == "__main__":
	N = int(input())
	line = list(map(int,input().split()))
	print(solution(line))