answer = [0]

def dfs(num,idx,total,goal):
    if total > goal:
        return
    elif total == goal:
        answer[0] += 1
        return
    else:
        for i in range(idx,len(num)):
            dfs(num,i+1,total+num[i],goal)

def solution():
    T = int(input())
    for t in range(1,T+1):
        N, K = map(int,input().split())
        answer[0] = 0
        num = list(map(int,input().split()))
        dfs(num,0,0,K)
        print(f'#{t} {answer[0]}')

if __name__ == "__main__":
    solution()