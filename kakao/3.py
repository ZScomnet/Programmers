def solution(fees,records):
	park_log = dict()
	for record in records:
		time,num,state = record.split()
		time = int(time[:2]) * 60 + int(time[3:5])
		if num not in park_log:
			park_log[num] = []
		park_log[num].append(time)

	carlist = sorted(park_log.keys())
	answer = []

	for number in carlist:
		total = 0
		if len(park_log[number]) % 2 == 1:
			park_log[number].append(23*60+59)
		for i in range(0,len(park_log[number]),2):
			total += park_log[number][i+1]-park_log[number][i]
		if total <= fees[0]:
			answer.append(fees[1])
		else:
			price = fees[1]
			total -= fees[0]
			price += (total // fees[2]) * fees[3]
			if total % fees[2] != 0:
				price += fees[3]
			answer.append(price)

	return answer

if __name__ == "__main__":
	print(solution([120, 0, 60, 591],["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))