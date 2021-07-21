import decimal
def solution(lines):
	result = 0
	time_line = []
	for time in lines:
		part = time.split()
		part[1] = part[1].split(':')
		part[2] = part[2][:-1]
		right = ""
		for i in part[1]:
			right += i
		right = float(right)
		part[2] = float(part[2])
		left = right - part[2]
		if int(left)%100 > 90:
			left -= 40
		if int(left)%10000 > 9000:
			left -= 4000
		
		left = decimal.Decimal(str(left))+decimal.Decimal('0.001')
		time_line.append([left,right])

	for time in time_line:
		left,right = time[1],decimal.Decimal(str(time[1]))+decimal.Decimal('0.999')
		if int(right)%100 >= 60:
			right -= 60
			right += 100
		if int(right)%10000 >= 6000:
			right -= 6000
			right += 10000
		
		count = 0
		for log in time_line:
			if left <= log[0] <= right or left <= log[1] <= right or (log[0] <= left and right <= log[1]):
				count += 1
		if result < count:
			result = count

	return result

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))