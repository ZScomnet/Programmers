# import heapq

# def solution(alp, cop, problems):
# 	q = []
# 	answer = 1e9
# 	max_alp,max_cop = 0,0
# 	for problem in problems:
# 		max_alp = max(max_alp,problem[0])
# 		max_cop = max(max_cop,problem[1])

# 	problems.append([0,0,1,0,1])
# 	problems.append([0,0,0,1,1])
# 	heapq.heappush(q,[0,alp,cop])
# 	while q:
# 		time,a,c = heapq.heappop(q)
# 		if time > answer:
# 			break
# 		if a >= max_alp and c >= max_cop:
# 			answer = min(time,answer) 

# 		for problem in problems:
# 			if problem[0] <= a and problem[1] <= c:
# 				heapq.heappush(q,[time+problem[4],a+problem[2],c+problem[3]])
# 	return answer

# def solution(alp, cop, problems):
# 	dp = [[1e9]*151 for _ in range(151)]
# 	dp[alp][cop] = 0
# 	answer = 1e9
# 	max_alp,max_cop = 0,0
# 	for problem in problems:
# 		max_alp = max(max_alp,problem[0])
# 		max_cop = max(max_cop,problem[1])

# 	for i in range(151):
# 		for j in range(i+1):
# 			if alp+i-j > 150 or cop+j > 150:
# 				continue
# 			if alp+i-j >= max_alp and cop+j >= max_cop:
# 				answer = min(answer, dp[alp+i-j][cop+j])
# 			dp[alp+i-j][cop+j] = min(dp[alp][cop]+i,dp[alp+i-j][cop+j])
# 			for problem in problems:
# 				if alp+i-j+problem[2] > 150 or cop+j+problem[3] > 150:
# 					continue
# 				if alp+i-j >= problem[0] and cop+j >= problem[1]:
# 					dp[alp+i-j+problem[2]][cop+j+problem[3]] = min(dp[alp+i-j+problem[2]][cop+j+problem[3]],dp[alp+i-j][cop+j]+problem[4])

# 	return answer

def solution(alp, cop, problems):
	max_alp,max_cop = 0,0
	for problem in problems:
		max_alp = max(max_alp,problem[0])
		max_cop = max(max_cop,problem[1])

	dp = [[1e9]*(max_cop+1) for _ in range(max_alp+1)]
	dp[alp][cop] = 0
	alp,cop = min(alp,max_alp), min(cop,max_cop)
	for i in range(alp,max_alp+1):
		for j in range(cop,max_cop+1):
			if i+1 <= max_alp:
				dp[i+1][j] = min(dp[i][j]+1,dp[i+1][j])
			if j+1 <= max_cop:
				dp[i][j+1] = min(dp[i][j]+1,dp[i][j+1])
			for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
				if i >= alp_req and j >= cop_req:
					a,c = min(max_alp,i+alp_rwd), min(max_cop,j+cop_rwd)
					dp[a][c] = min(dp[a][c],dp[i][j]+cost)
	return dp[max_alp][max_cop]


if __name__ == "__main__":
	print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))