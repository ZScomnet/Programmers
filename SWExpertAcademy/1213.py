def solution():
    T = 10
    for t in range(1,T+1):
        input()
        find = input()
        string = input()
        answer = 0
        for i in range(len(string)-len(find)+1):
            if string[i:i+len(find)] == find:
                answer += 1
        print(f'#{t} {answer}')

if __name__ == "__main__":
    solution()