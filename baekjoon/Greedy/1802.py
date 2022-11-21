import sys
input = sys.stdin.readline

def isDivide(line):
	line = list(line)
	while len(line) >= 3:
		for i in range(2,len(line),2):
			if line[i-2] == line[i]:
				return False
		nextLine = []
		for i in range(1,len(line),2):
			nextLine.append(line[i])
		line = nextLine
	return True
def solution():
	N = int(input())
	for _ in range(N):
		line = input().rstrip()
		if isDivide(line):
			print("YES")
		else:
			print("NO")

if __name__ == "__main__":
	solution()