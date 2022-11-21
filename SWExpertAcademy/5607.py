def MOD(N,mod):
	if mod == 0:
		return 1
	if mod%2 == 1:
		return (MOD(N,mod-1)*N) % 1234567891
	half = MOD(N,int(mod/2)) % 1234567891
	return (half * half) % 1234567891

def solution():
    T = int(input())
    for t in range(1,T+1):
        N, K = map(int, input().split())
        mod = 1234567891
        answer, m = 1, 1
        for n in range(N):
            answer *= n + 1
            answer %= mod
        for k in range(K):
            m *= k + 1
            m %= mod
        for k in range(N - K):
            m *= k + 1
            m %= mod
        m = MOD(m, mod - 2)
        answer *= m
        answer %= mod

        print(f'#{t} {answer}')

if __name__ == "__main__":
    solution()