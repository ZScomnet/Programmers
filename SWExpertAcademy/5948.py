def solution():
    T = int(input())
    for t in range(1,T+1):
        num = list(map(int,input().split()))
        memory = [0]*301
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                for k in range(j+1,len(num)):
                    memory[num[i]+num[j]+num[k]] = 1
        cnt = 0
        for i in range(300,-1,-1):
            if memory[i] == 1:
                cnt += 1
            if cnt == 5:
                print(f'#{t} {i}')
                break
if __name__ == "__main__":
    solution()