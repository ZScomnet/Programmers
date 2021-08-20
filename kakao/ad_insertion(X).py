def solution(play_time,adv_time,logs):
	h,m,s = play_time.split(':')
	play_time = int(h) * 3600 + int(m) * 60 + int(s)
	h,m,s = adv_time.split(':')
	adv_time = int(h) * 3600 + int(m) * 60 + int(s)
	timeline = [0 for _ in range(play_time+1)]
	total_time = [0 for _ in range(play_time+1)]
	max_time = 0

	for log in logs:
		left,right = log.split('-')
		h,m,s = left.split(':')
		start = int(h) * 3600 + int(m) * 60 + int(s)
		h,m,s = right.split(':')
		end = int(h) * 3600 + int(m) * 60 + int(s)
		for i in range(start,end):
			timeline[i] += 1

	for i in range(1,play_time+1):
		total_time[i] = total_time[i-1] + timeline[i]

	start = 0
	total = 0
	for i in range(0,play_time-adv_time):
		if total_time[adv_time+i]-total_time[i] > total:
			total = total_time[adv_time+i]-total_time[i]
			start = i+1
	answer = ""
	if start // 3600 < 10:
		answer += "0"
	answer += str(start//3600) + ":"
	if (start%3600) // 60 < 10:
		answer += "0"
	answer += str((start%3600)//60) + ":"
	if (start%3600) % 60 < 10:
		answer += "0"
	answer += str((start%3600)%60)
	return answer
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))