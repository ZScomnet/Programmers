import sys
input = sys.stdin.readline

def solution():
    s1 = input().strip()
    s2 = input().strip()
    start,end = 0,1
    answer = 0
    while start < len(s1):
        s = s1[start:end]
        if s in s2:
            answer = max(answer,len(s))
            end += 1
            if end > len(s1):
                break
        else:
            start += 1
            if start == end:
                end += 1
    return answer

if __name__ == "__main__":
    print(solution())