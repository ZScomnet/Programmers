from collections import deque
def solution():
    T = 10
    for t in range(1,T+1):
        answer = 0
        board = []
        input()
        q = deque()
        for row in range(100):
            board.append(list(map(int,input().split())))
            for col in range(100):
                if board[row][col] != 0:
                    q.append([row,col])
        while q:
            row,col = q.popleft()
            if board[row][col] == 1:
                for drow in range(row+1,100):
                    if board[drow][col] == 1:
                        break
                    elif board[drow][col] == 2:
                        answer += 1
                        break
            elif board[row][col] == 2:
                for drow in range(row-1,-1,-1):
                    if board[drow][col] == 2:
                        break
                    elif board[drow][col] == 1:
                        answer += 1
                        break
        print(f'#{t} {answer//2}')

if __name__ == "__main__":
    solution()