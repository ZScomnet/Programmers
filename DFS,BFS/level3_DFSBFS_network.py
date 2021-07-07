def DFS(computers,counter,com_num):
	for i in range(len(computers[com_num])):
		if computers[com_num][i] == 1 and counter[i] == 0:
			counter[i] = 1
			DFS(computers,counter,i)


def solution(n,computers):
	counter = [0]*n
	result = 0
	for i in range(n):
		if counter[i] != 0:
			continue
		counter[i] = 1
		DFS(computers,counter,i)
		result += 1
	return result

print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))