from collections import deque
def solution():
    T = int(input())
    for t in range(1,T+1):
        n, m = map(int,input().split())
        answer = 0
        cost = []
        for _ in range(n):
            cost.append(int(input()))
        cars = [-1]
        for _ in range(m):
            cars.append(int(input()))
        parking = [0] * n
        q = deque()
        for _ in range(m*2):
            commandCarIdx = int(input())
            if commandCarIdx < 0:
                commandCarIdx *= -1
                for i in range(n):
                    if parking[i] == commandCarIdx:
                        parking[i] = 0
                        if q:
                            parking[i] = q.popleft()
                            answer += cost[i] * cars[parking[i]]
                        break

            else:
                if q:
                    q.append(commandCarIdx)
                else:
                    isFull = True
                    for i in range(n):
                        if parking[i] == 0:
                            parking[i] = commandCarIdx
                            answer += cost[i] * cars[commandCarIdx]
                            isFull = False
                            break
                    if isFull:
                        q.append(commandCarIdx)
        print(f'#{t} {answer}')


if __name__ == "__main__":
    solution()