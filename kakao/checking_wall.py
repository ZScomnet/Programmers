from itertools import combinations

def solution(n,weak,dist):
	weak_term = [n-weak[-1]+weak[0]]+[abs(weak[i-1] - weak[i]) for i in range(1,len(weak))]
	dist = sorted(dist,reverse=True)
	answer = -1
	length = 0
	for i in range(len(dist)):
		com = list(combinations(weak_term,len(weak)-i-1))
		length += dist[i]
		for time in com:
			if length >= sum(list(time)):
				answer = i+1
				break
		if answer != -1:
			break
	return answer

if __name__ == "__main__":
	print(solution(200,[0,50,100,150],[10,10,10,10]))