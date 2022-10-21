import sys
input = sys.stdin.readline

def solution(s):
	dp = [0] * (len(s)-1)
	dp[0] = 1
	if s[0] == "0":
		return 0
	if len(s)-1 == 1:
		return 1
	dp[1] = 1
	if int(s[0]+s[1]) <= 26 and int(s[0]+s[1]) % 10 != 0:
		dp[1] += 1
	elif int(s[0]+s[1]) > 26 and int(s[0]+s[1]) % 10 == 0:
		return 0
	for i in range(2,len(s)-1):
		if s[i] == "0":
			dp[i-1] = dp[i-2]
			dp[i] = dp[i-1]
			if int(s[i-1]+s[i]) > 26 or int(s[i-1]+s[i]) == 0:
				return 0
			continue
		dp[i] = dp[i-1]
		if int(s[i-1]+s[i]) <= 26 and s[i-1] != "0":
			dp[i] += dp[i-2]
		dp[i] %= 1000000
	return dp[-1]

if __name__ == "__main__":
	print(solution(input()))