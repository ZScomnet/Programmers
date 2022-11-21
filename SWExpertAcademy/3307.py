def solution():
    T = int(input())
    for t in range(1,T+1):
        answer = 1
        N = int(input())
        num = list(map(int,input().split()))
        dp = [1]*N
        for i in range(N):
            for j in range(i+1,N):
                if num[i] < num[j]:
                    dp[j] = max(dp[j],dp[i]+1)
            answer = max(dp[i],answer)
        print(f'#{t} {answer}')


if __name__ == "__main__":
    solution()