import sys
import heapq
input = sys.stdin.readline

tickets = []

def solution(N,M,K):
	answer = 1e9
	q = []
	for ticket in tickets[0]:
		v,c,d = ticket
		heapq.heappush(q,[d,c,v,[0,v]])

	while q:
		print(q)
		time,cost,now,check = heapq.heappop(q)
		if now == N-1 and cost <= M:
			answer = min(answer,time)
		else:
			for i in tickets[now]:
				v,c,d = i
				if v not in check:
					check.append(v)
					heapq.heappush(q,[time+d,cost+c,v,check])
					check.pop()

	if answer == 1e9:
		return "Poor KCM"
	else:
		return answer
	
if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		N,M,K = map(int,input().split())
		for _ in range(N):
			tickets.append([])
		for _ in range(K):
			u,v,c,d = map(int,input().split())
			tickets[u-1].append([v-1,c,d])
		print(solution(N,M,K))
		tickets = []