def solution():
    T = 10
    for t in range(1,T+1):
        answer = 0
        board = []
        input()
        for _ in range(100):
            board.append(list(map(int,input().split())))
            answer = max(sum(board[-1]),answer)

        for col in range(100):
            result = 0
            for row in range(100):
                result += board[row][col]
            answer = max(result,answer)
        left,right = 0,0
        for i in range(100):
            left += board[i][i]
            right += board[99-i][99-i]
        answer = max(left,right,answer)
        print(f'#{t} {answer}')

if __name__ == "__main__":
    solution()