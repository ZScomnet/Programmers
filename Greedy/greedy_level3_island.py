def is_cycle(check,island):
	if check[island] == island:
		return island
	else:
		return is_cycle(check,check[island])


def solution(n,cost):
	cost = sorted(cost,key = lambda cost_data : cost_data[2])
	check = [i for i in range(n)]
	result = 0
	for bridge in cost:
		island1,island2,price = bridge[0],bridge[1],bridge[2]
		if is_cycle(check,island1) != is_cycle(check,island2):
			result += price
			if check[island1] < check[island2]:
				child = check[island2]
				for i in range(len(check)):
					if check[i] == child:
						check[i] = check[island1]
			else:
				child = check[island1]
				for i in range(len(check)):
					if check[i] == child:
						check[i] = check[island2]

	return result

print(solution(5,[[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]))