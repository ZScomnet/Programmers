def search(db,costs,load,s,loads,prices,price):
	if load[-1] == s:
		db.append(load.copy()[::-1])
		costs.append(price)
	else:
		for way,cost in zip(loads[load[-1]],prices[load[-1]]):
			if way not in load:
				load.append(way)
				search(db,costs,load,s,loads,prices,price+cost)
				load.pop()


def solution(n,s,a,b,fares):
	loads = dict()
	prices = dict()
	for i in range(1,n+1):
		loads[i] = []
		prices[i] = []
	for load in fares:
		loads[load[0]].append(load[1])
		loads[load[1]].append(load[0])
		prices[load[0]].append(load[2])
		prices[load[1]].append(load[2])
	
	a_loads = []
	a_costs = []
	search(a_loads,a_costs,[a],s,loads,prices,0)
	b_loads = []
	b_costs = []
	search(b_loads,b_costs,[b],s,loads,prices,0)
	answer = 0
	for a_load in a_loads:
		for b_load in b_loads:
			cost = 0
			dual_index = 0
			for i in range(1,min(len(a_load),len(b_load))):
				if a_load[i] == b_load[i]:
					for load,price in zip(loads[a_load[i-1]],prices[a_load[i-1]]):
						if load == a_load[i]:
							cost += price
							dual_index+=1
							break
				else:
					break
			for i in range(1+dual_index,len(a_load)):
				for load,price in zip(loads[a_load[i-1]],prices[a_load[i-1]]):
					if load == a_load[i]:
						cost += price
						break
			for i in range(1+dual_index,len(b_load)):
				for load,price in zip(loads[b_load[i-1]],prices[b_load[i-1]]):
					if load == b_load[i]:
						cost += price
						break
			if answer == 0 or cost < answer:
				answer = cost
			
	return answer

print(solution(6,4,6,2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))