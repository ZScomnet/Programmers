def solution():
    T = 10
    for t in range(1,T+1):
        answer = 0
        board = []
        N = int(input())
        for _ in range(8):
            board.append(list(input()))
        for row in range(8):
            for start in range(0,9-N):
                if board[row][start:start+N] == board[row][start:start+N][::-1]:
                    answer += 1
        for col in range(8):
            for start in range(0,9-N):
                s1,s2 = "",""
                for i in range(N):
                    s1 += board[start+i][col]
                    s2 += board[start+N-1-i][col]
                if s1 == s2:
                    answer += 1
        print(f'#{t} {answer}')

if __name__ == "__main__":
    solution()