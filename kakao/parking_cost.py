def solution(fees, records):
	cost = dict()
	park = dict()
	for record in records:
		time,num,state = record.split(" ")
		hour,sec = time.split(":")
		time = int(hour) * 60 + int(sec)
		if state == "IN":
			park[num] = time
		else:
			if num in cost:
				cost[num] += time - park[num]
				park[num] = -1
			else:
				cost[num] = time - park[num]
				park[num] = -1
	for key,value in zip(park.keys(),park.values()):
		if value != -1:
			if key in cost:
				cost[key] += (23*60+59) - value
			else:
				cost[key] = (23*60+59) - value
	answer = []
	for key in sorted(cost.keys()):
		if cost[key] <= fees[0]:
			answer.append(fees[1])
		else:
			if (cost[key]-fees[0]) % fees[2] == 0:
				answer.append(fees[1] + ((cost[key]-fees[0]) // fees[2]) * fees[3])
			else:
				answer.append(fees[1] + (((cost[key]-fees[0]) // fees[2])+1) * fees[3])
	return answer

if __name__ == "__main__":
	print(solution([1,461,1,10],["00:00 1234 IN"]))