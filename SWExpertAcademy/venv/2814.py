answer = [1]

def search(graph,visited,now,depth):
    answer[0] = max(answer[0], depth)
    for i in range(len(graph)):
        if visited[i] == 0 and graph[now][i] == 1:
            visited[i] = 1
            search(graph,visited,i,depth+1)
            visited[i] = 0

def solution():
    T = int(input())
    for t in range(1,T+1):
        N, M = map(int,input().split())
        graph = [[0]*(N+1) for _ in range(N+1)]
        answer[0] = 1
        for _ in range(M):
            start,end = map(int,input().split())
            graph[start][end] = 1
            graph[end][start] = 1

        for i in range(1,N+1):
            visited = [0] * (N+1)
            visited[i] = 1
            search(graph,visited,i,1)

        print(f'#{t} {answer[0]}')

if __name__ == "__main__":
    solution()