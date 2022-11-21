T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    building = list(map(int,input().split()))
    answer = 0
    for i in range(N):
        max_h = 0
        for j in range(-2,3):
            if 0 <= i+j < N and j != 0:
                max_h = max(max_h,building[i+j])
        if building[i] - max_h > 0:
            answer += building - max_h
    print(f'#{test_case} {answer}')