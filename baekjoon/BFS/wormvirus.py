import sys
input = sys.stdin.readline

def solution(dic):
	depth = [1]
	counter = [0] * len(dic)
	counter[0] = 1
	while depth:
		next_depth = []
		for i in depth:
			for n in dic[i]:
				if counter[n-1] == 0:
					counter[n-1] = 1
					next_depth.append(n)
		depth = next_depth
	return sum(counter)-1

if __name__ == "__main__":
	node = int(input())
	edge = int(input())
	dic = dict()
	for i in range(node):
		dic[i+1] = []
	for _ in range(edge):
		start,end = map(int,input().split())
		dic[start].append(end)
		dic[end].append(start)
	print(solution(dic))