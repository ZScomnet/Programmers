def solution(jobs):
	now = 0
	len_jobs = len(jobs)
	jobs.sort()
	d_cnt = True
	result = 0
	while len(jobs) != 0:
		if d_cnt:
			req_time = []
			pro_time = []
			for i in jobs:
				if i[0] > now:
					break
				req_time.append(i[0])
				pro_time.append(i[1])
				if req_time[-1] == jobs[-1][0]:
					d_cnt = False
		if len(req_time) == 0:
			now += 1
		else:
			index = pro_time.index(min(pro_time))
			result += now - req_time[index] + pro_time[index]
			now += pro_time[index]
			del jobs[index]
			del pro_time[index]
			del req_time[index]

	return int(result/len_jobs) 

print(solution([[10,10]]))