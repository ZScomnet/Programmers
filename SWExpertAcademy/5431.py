from collections import deque

def solution():
    T = int(input())
    for t in range(1,T+1):
        N, K = map(int,input().split())
        report = deque(sorted(list(map(int,input().split()))))
        students = deque([i for i in range(1,N+1)])
        print(f'#{t} ',end='')
        while students:
            if len(report) == 0:
                print(students.popleft(), end='')
                if students:
                    print(' ', end='')
            elif report[0] == students[0]:
                report.popleft()
                students.popleft()
            else:
                print(students.popleft(),end='')
                if students:
                    print(' ',end='')
        print()

if __name__ == "__main__":
    solution()