from collections import deque

def solution():
    T = int(input())
    for t in range(1,T+1):
        N,M,K = map(int,input().split())
        customers = deque(sorted(list(map(int,input().split()))))
        answer = "Possible"
        cnt = 0
        while customers:
            time = customers.popleft()
            cnt += 1
            bread = (time//M)*K
            if bread-cnt < 0:
                answer = "Impossible"
                break
        print(f'#{t} {answer}')

if __name__ == "__main__":
    solution()