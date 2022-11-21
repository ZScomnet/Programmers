def solution():
    prime = [0]*1000001
    print("2 ",end='')
    for i in range(3,1000001,2):
        if prime[i] == 0:
            print(i,end='')
            if i < 999983:
                print(' ',end='')
            for j in range(i,1000001,i):
                prime[j] = 1

if __name__ == "__main__":
    solution()