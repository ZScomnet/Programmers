from collections import deque
import sys
input = sys.stdin.readline

def melt(board,R,C):
    nextBoard = [[0]*C for _ in range(R)]
    for row in range(R):
        for col in range(C):
            if board[row][col] != 0:
                meltPoint = 0
                for drow,dcol in zip([-1,0,1,0],[0,1,0,-1]):
                    if 0 <= row+drow < R and 0 <= col+dcol < C:
                        if board[row+drow][col+dcol] == 0:
                            meltPoint += 1
                nextBoard[row][col] = max(0,board[row][col]-meltPoint)
    return nextBoard

def solution():
    R,C = map(int,input().split())
    board = []
    for _ in range(R):
        board.append(list(map(int,input().split())))
    zeroCnt = 0
    answer = 0
    while zeroCnt != R*C:
        visited = [[0]*C for _ in range(R)]
        glacier = 0
        zeroCnt = 0
        for row in range(R):
            for col in range(C):
                if board[row][col] != 0 and visited[row][col] == 0:
                    visited[row][col] = 1
                    q = deque([[row,col]])
                    while q:
                        r,c = q.popleft()
                        for dr,dc in zip([-1,0,1,0],[0,1,0,-1]):
                            if 0 <= r+dr < R and 0 <= c+dc < C:
                                if board[r+dr][c+dc] != 0 and visited[r+dr][c+dc] == 0:
                                    visited[r+dr][c+dc] = 1
                                    q.append([r+dr,c+dc])
                    glacier += 1
                else:
                    zeroCnt += 1
        if glacier > 1:
            return answer
        board = melt(board, R, C)
        answer += 1
    return 0

if __name__ == "__main__":
    print(solution())