import sys
sys.setrecursionlimit(100001)

answer = []

def search(depth,dic,now,stack):
	if len(stack) == depth:
		answer.append(stack.copy())
		return
	elif now in dic:
		for i in range(len(dic[now])):
			if dic[now][i] != "-":
				temp = dic[now][i]
				dic[now][i] = "-"
				stack.append(temp)
				search(depth,dic,temp,stack)
				dic[now][i] = temp
				stack.pop()

def solution(tickets):
	dic = dict()
	for i in tickets:
		start,end = i
		if start not in dic:
			dic[start] = []
		dic[start].append(end)
	search(len(tickets)+1,dic,"ICN",["ICN"])

	return sorted(answer)[0]

if __name__ == "__main__":
	print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))