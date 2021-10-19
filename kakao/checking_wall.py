def checkwall(n,weak,dist,db):
	if len(weak) == 0:
		if db[0] < len(dist):
			db[0] = len(dist)

	else:
		for d in range(len(dist)):
			for w in range(len(weak)):
				find_weak = []
				start = weak[w]
				for point in weak:
					if start+dist[d] > n:
						if start+dist[d]-n < point < start:
							find_weak.append(point)
					else:
						if point < start or start+dist[d] < point:
							find_weak.append(point)
					
				dist_copy = dist.copy()
				del dist_copy[d]
				checkwall(n,find_weak,dist_copy,db)

def solution(n,weak,dist):
	db = [-1]
	checkwall(n,weak,dist,db)
	if db[0] == -1:
		return -1
	else:
		return len(dist) - db[0]

if __name__ == "__main__":
	print(solution(12,[1,5,6,10],[1,2,3,4]))