from collections import deque

def num(x,y):
    num = 1
    for i in range(1,y):
        num += i
    for i in range(1,x):
        num += y+i
    return num

def point(num):
    left,right = 0,0
    for i in range(1,10000):
        left,right = right,right+i
        if left < num <= right:
            return [num-left,i-(num-left)+1]

def solution():
    T = int(input())
    for t in range(1,T+1):
        p,q = map(int,input().split())
        px,py = point(p)
        qx,qy = point(q)
        x,y = px+qx, py+qy
        answer = num(x,y)
        print(f'#{t} {answer}')

if __name__ == "__main__":
    solution()