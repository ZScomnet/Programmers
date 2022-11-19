def attack(board,row,col,c):
    dic = {1 : 'B', 2 : 'W'}
    N = len(board)-1
    color = dic[c]
    board[row][col] = color
    way = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(1,len(board)):
        for drow,dcol in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]):
            if 0 < row+drow*i < N and 0 < col+dcol*i < N and way[1+drow][1+dcol] == 0:
                if board[row+drow*i][col+dcol*i] == 0 and way[1+drow][1+dcol] == 0:
                    way[1+drow][1+dcol] = -1
                elif board[row+drow*i][col+dcol*i] == color and way[1+drow][1+dcol] == 0:
                    way[1+drow][1+dcol] = 1
    for drow,dcol in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]):
        if way[1+drow][1+dcol] == 1:
            for i in range(1,N):
                if board[row+drow*i][col+dcol*i] != color:
                    board[row+drow*i][col+dcol*i] = color
                else:
                    break
    return board

def solution():
    T = int(input())
    for t in range(1,T+1):
        black,white = 0,0
        N, M = map(int,input().split())
        board = [[0] * (N+2) for _ in range(N+2)]
        board[N // 2][N // 2] = 'W'
        board[N // 2+1][N // 2] = 'B'
        board[N // 2][N // 2+1] = 'B'
        board[N // 2+1][N // 2+1] = 'W'
        for _ in range(M):
            row,col,c = map(int,input().split())
            board = attack(board,row,col,c)
        for row in range(1,N+1):
            for col in range(1,N+1):
                if board[row][col] == 'B':
                    black += 1
                elif board[row][col] == 'W':
                    white += 1

        print(f'#{t} {black} {white}')

if __name__ == "__main__":
    solution()