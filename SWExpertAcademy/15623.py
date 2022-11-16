import heapq

T = int(input())
for test_case in range(1, T + 1):
    V,E = map(int,input().split())
    graph = dict()
    for _ in range(E):
    	start,end,v1,v2 = map(int,input().split())
    	if start in graph:
    		graph[start].append([end,v1+v2])
    	else:
    		graph[start] = [[end,v1+v2]]
    	if end in graph:
    		graph[end].append([start,v1+v2])
    	else:
    		graph[end] = [[start,v1+v2]]
    q = [[1,1]]
    visited = [1e9] * (V+1)
    visited[1] = 0
    answer = 0
    while q:
    	cost, now = heapq.heappop(q)
    	if visited[now] < cost and now != 1:
    		continue
    	if now == 2:
    		answer = cost
    		continue
    	if now in graph:
    		for v in graph[now]:
    			n,c = v
    			if visited[n] > cost*c:
    				visited[n] = cost*c
    				heapq.heappush(q,[cost*c,n])
    if answer == 0:
    	answer = -1
    print(f"#{test_case} {answer}")