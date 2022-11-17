def solution():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        answer = 0
        mid = N // 2
        for i in range(N):
            line = list(map(int,list(input())))
            if i <= mid:
                answer += sum(line[mid-i:mid+1+i])
            else:
                answer += sum(line[i-mid:N-(i-mid)])
        print(f'#{t} {answer}')

if __name__ == "__main__":
    solution()