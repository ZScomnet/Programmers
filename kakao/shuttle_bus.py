def solution(n,t,m,timetable):
	num_timetable = sorted([int(time[0:2]+time[3:5]) for time in timetable])
	bus_time = [900]
	for i in range(n-1):
		next_bus = bus_time[-1] + t
		if next_bus % 100 >= 60:
			next_bus += 40
		bus_time.append(next_bus)
	last_cru = []
	for time in bus_time:
		count = 0
		index = 0
		while count != m and num_timetable and index < len(num_timetable):
			if num_timetable[index] <= time:
				count += 1
				if time == bus_time[-1] and len(last_cru) != m:
					last_cru.append(num_timetable[index])
				del num_timetable[index]
			else:
				index += 1
		if last_cru:
			break
	if len(last_cru) < m:
		if bus_time[-1] < 1000:
			return "0"+str(bus_time[-1]//100)+ ":" + str(bus_time[-1])[1:]
		else:
			return str(bus_time[-1]//100)+ ":" + str(bus_time[-1])[2:]

	else:
		result = last_cru[-1] - 1
		if result % 100 == 99:
			result -= 40
		if result < 1000:
			answer = "0"+str(result//100)+ ":"
		else:
			answer = str(result//100)+ ":"
		if result % 100 == 0:
			return answer+"00"
		elif 0 < result % 100 < 10:
			return answer+"0"+str(result)[-1]
		else:
			return answer+str(result%100)

print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))