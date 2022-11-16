def isInWeb(q0,q1,q2,q):
    x1, y1, z1 = q0
    x2, y2, z2 = q1
    x3, y3, z3 = q2

    a = y1*(z2-z3) + y2*(z3-z1) + y3*(z1-z2)
    b = z1*(x2-x3) + z2*(x3-x1) + z3*(x1-x2)
    c = x2*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
    d = -1*(x1*(y2*x3 - y3*z2) + x2*(y3*x1 - y1*z3) + x3*(y1*x2 - y2*z1))
    if a*q[0] + b*q[1] + c*q[2] + d == 0:
        return True
    else:
        return False

def print_hi():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        q = []
        for i in range(N):
            q.append(list(map(int,input().split())))
        if N <= 3:
            print(f'#{test_case} TAK')
        else:
            isWeb = True
            for i in range(3,len(q)):
                if isInWeb(q[0],q[1],q[2],q[i]):
                    isWeb = True
                else:
                    isWeb = False
            if isWeb:
                print(f'#{test_case} TAK')
            else:
                print(f'#{test_case} NIE')

if __name__ == '__main__':
    print_hi()