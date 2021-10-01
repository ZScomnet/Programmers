import sys
input = sys.stdin.readline

def solution(line):
	data = [0]*len(line)
	data[0] = line[0]
	for idx in range(1,len(line)):
		data[idx] = max(line[idx],data[idx-1]+line[idx])

	return max(data)

if __name__ == "__main__":
	N = int(input())
	line = list(map(int,input().split()))
	print(solution(line))