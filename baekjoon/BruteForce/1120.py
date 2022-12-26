def solution():
	a,b = input().split()
	maxEqual = 0
	for start in range(len(b)-len(a)+1):
		cnt = 0
		for i in range(len(a)):
			if a[i] == b[start+i]:
				cnt += 1
		maxEqual = max(cnt,maxEqual)

	return len(a)-maxEqual

if __name__ == "__main__":
	print(solution())