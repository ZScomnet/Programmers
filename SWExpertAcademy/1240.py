def solution():
    T = int(input())
    for t in range(1,T+1):
        answer = 0
        R,C = map(int,input().split())
        dic = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
        code = []
        for _ in range(R):
            code.append(input())
        sr,sc = -1,-1
        for row in range(R):
            for col in range(C-56+1):
                if code[row][col:col+7] in dic:
                    check = True
                    for i in range(0,56,7):
                        if code[row][col+i:col+i+7] not in dic:
                            check = False
                            break
                    if check:
                        sr,sc = row,col
                        break
            if sr != -1:
                break
        password = []
        for col in range(sc,sc+56,7):
            password.append(dic[code[sr][col:col+7]])
        result = (password[0] + password[2] + password[4] + password[6]) * 3 + password[1]+password[3]+password[5]+password[7]
        if result % 10 == 0:
            answer = sum(password)

        print(f'#{t} {answer}')

if __name__ == "__main__":
    solution()