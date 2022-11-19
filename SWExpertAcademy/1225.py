from collections import deque

def solution():
    T = 10
    for t in range(1,T+1):
        input()
        num = deque(list(map(int,input().split())))
        while num[-1] != 0:
            for i in range(1,6):
                num.append(num.popleft()-i)
                if num[-1] <= 0:
                    num[-1] = 0
                    break

        print(f'#{t}',end=' ')
        for i in num:
            print(i,end='')
            if i != 0:
                print(' ',end='')
        print()


if __name__ == "__main__":
    solution()