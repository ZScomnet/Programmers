def solution():
    T = int(input())
    for t in range(1,T+1):
        N, K = map(int,input().split())
        item = []
        for _ in range(N):
            item.append(list(map(int,input().split())))
        dp = [[0] * (K+1) for _ in range(N+1)]
        for row in range(1,N+1):
            v,c = item[row-1]
            for col in range(1,K+1):
                if col == v:
                    dp[row][col] = max(dp[row][col-1],dp[row-1][col],c)
                elif col-v > 0:
                    dp[row][col] = max(dp[row][col-1],dp[row-1][col],dp[row-1][col-v]+c)
                else:
                    dp[row][col] = max(dp[row-1][col],dp[row][col-1])
        print(f'#{t} {dp[-1][-1]}')

if __name__ == "__main__":
    solution()