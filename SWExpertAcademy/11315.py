def bfs(board,row,col):
    N = len(board)
    for drow,dcol in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]):
        cnt = 0
        for i in range(1,5):
            if 0 <= row+drow*i < N and 0 <= col+dcol*i < N:
                if board[row+drow*i][col+dcol*i] == 'o':
                    cnt += 1
        if cnt == 4:
            return True
    return False

def solution():
    T = int(input())
    for t in range(1,T+1):
        answer = 'NO'
        N = int(input())
        board = []
        for _ in range(N):
            board.append(list(input()))
        isBingo = False
        for row in range(N):
            for col in range(N):
                if board[row][col] == 'o':
                    isBingo = bfs(board,row,col)
                if isBingo:
                    answer = 'YES'
                    break
            if isBingo:
                break
        print(f'#{t} {answer}')


if __name__ == "__main__":
    solution()