T = int(input())
for t in range(1,T+1):
    n = int(input())
    if n%2 == 0:
        print(f'#{t} Bob')
    else:
        print(f'#{t} Alice')