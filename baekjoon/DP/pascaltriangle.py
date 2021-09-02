def MOD(m,mod):
	if mod == 0:
		return 1
	if mod%2 == 1:
		return (MOD(m,mod-1)*N) % 1000000007
	half = MOD(m,int(mod/2)) % 1000000007
	return (half * half) % 1000000007

if __name__ == "__main__":
	N,K = map(int,input().split())
	mod = 1000000007
	answer,m = 1,1
	for n in range(N):
		answer *= n+1
		answer %= mod
	for k in range(K):
		m *= k+1
		m %= mod
	for k in range(N-K):
		m *= k+1
		m %= mod
	m = MOD(m,mod-2)
	answer *= m
	answer %= mod
	print(answer)