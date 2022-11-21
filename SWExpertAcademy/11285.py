def solution():
    T = int(input())
    score = [[0]*201 for _ in range(201)]
    for row in range(201):
        for col in range(201):
            length = (row*row+col*col) ** (1/2)
            if length <= 20:
                score[row][col] = 10
            elif length <= 40:
                score[row][col] = 9
            elif length <= 60:
                score[row][col] = 8
            elif length <= 80:
                score[row][col] = 7
            elif length <= 100:
                score[row][col] = 6
            elif length <= 120:
                score[row][col] = 5
            elif length <= 140:
                score[row][col] = 4
            elif length <= 160:
                score[row][col] = 3
            elif length <= 180:
                score[row][col] = 2
            elif length <= 200:
                score[row][col] = 1
    for t in range(1,T+1):
        answer = 0
        N = int(input())
        for _ in range(N):
            x,y = map(int,input().split())
            answer += score[abs(x)][abs(y)]

        print(f'#{t} {answer}')


if __name__ == "__main__":
    solution()