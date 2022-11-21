import sys
input = sys.stdin.readline

def solution():
	T = int(input())
	for t in range(T):
		N = int(input())
		string = input().rstrip()
		maxString = ord('a')
		for i in string:
			maxString = max(maxString,ord(i))
		print(maxString-ord('a')+1)
if __name__ == "__main__":
	solution()
