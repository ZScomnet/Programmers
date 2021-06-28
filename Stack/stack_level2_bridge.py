def solution(bridge_length,weight,truck_weights):
	bridge_q = []
	fin_q = []
	time_q = []
	time = 0
	while len(bridge_q) != 0 or len(truck_weights) != 0:
		try:
			if time - time_q[0] == bridge_length:
				fin_q.append(bridge_q[0])
				del bridge_q[0]
				del time_q[0]
		except:
			pass

		try:
			if sum(bridge_q)+truck_weights[0] <= weight:
				bridge_q.append(truck_weights[0])
				time_q.append(time)
				del truck_weights[0]
		except:
			pass
		time += 1

	return time

print(solution(2,10,[7,4,5,6]))