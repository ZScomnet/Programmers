import sys
# import heapq
input = sys.stdin.readline
INF = float('inf')
# dijkstra
# def search(start,bus,N):
# 	q = []
# 	result = [INF] * (N+1) 
# 	heapq.heappush(q,[0,start])
# 	while q:
# 		cost,now = heapq.heappop(q)
# 		for edge in bus[now]:
# 			end,c = edge
# 			if result[end] > cost + c:
# 				result[end] = cost+c
# 				heapq.heappush(q,[cost+c,end])
# 	result[start] = 0
# 	for i in range(1,N+1):
# 		if result[i] == INF:
# 			result[i] = 0 
# 	return result

# def solution(bus,N,M):
# 	answer = []
# 	for i in range(1,N+1):
# 		answer.append(search(i,bus,N))
# 	for i in answer:
# 		for j in range(1,N+1):
# 			print(i[j],end=" ")
# 		print()
# floyd
def solution(bus,N,M):
	for i in range(1,N+1):
		bus[i][i] = 0
	for mid in range(1,N+1):
		for start in range(1,N+1):
			for end in range(1,N+1):
				bus[start][end] = min(bus[start][end],bus[start][mid]+bus[mid][end])
	for i in range(1,N+1):
		for j in range(1,N+1):
			if bus[i][j] != INF:
				print(bus[i][j],end=" ")
			else:
				print(0,end=" ")
		print()


if __name__ == "__main__":
	N = int(input())
	M = int(input())
	# bus = dict()
	# for i in range(1,N+1):
	# 	bus[i] = []
	# for _ in range(M):
	# 	start,end,cost = map(int,input().split())
	# 	bus[start].append([end,cost])
	bus = [[INF] * (N+1) for _ in range(N+1)]
	for _ in range(M):
		start,end,cost = map(int,input().split())
		bus[start][end] = min(cost,bus[start][end])
	
	solution(bus,N,M)