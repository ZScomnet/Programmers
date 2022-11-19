from collections import deque
def solution():
    T = 10
    for t in range(1,T+1):
        N = int(input())
        pw = list(map(int,input().split()))
        input()
        commands = deque(input().split())
        while commands:
            command = commands.popleft()
            if command == 'I':
                idx = int(commands.popleft())
                insertDeque = []
                for _ in range(int(commands.popleft())):
                    insertDeque.append(int(commands.popleft()))
                pw = pw[:idx]+insertDeque+pw[idx:]
            elif command == 'A':
                appendPw = int(commands.popleft())
                for _ in range(appendPw):
                    pw.append(int(commands.popleft()))
            else:
                idx = int(commands.popleft())
                deleteIdx = int(commands.popleft())
                pw = pw[:idx] + pw[idx+deleteIdx:]
        print(f'#{t} ',end='')
        for i in range(10):
            print(pw[i],end='')
            if i < 9:
                print(' ',end='')
        print()


if __name__ == "__main__":
    solution()