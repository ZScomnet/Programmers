def solution(line):
	min_x,max_x,min_y,max_y = 1e99,-1e99,1e99,-1e99
	point = []
	for i in range(len(line)):
		for j in range(i+1,len(line)):
			a,b,e = line[i]
			c,d,f = line[j]
			if a*d - b*c == 0:
				continue
			if (b*f-e*d) % (a*d-b*c) == 0 and (e*c-a*f) % (a*d-b*c) == 0:
				min_x = min((b*f-e*d)//(a*d-b*c),min_x)
				max_x = max((b*f-e*d)//(a*d-b*c),max_x)
				min_y = min((e*c-a*f)//(a*d-b*c),min_y)
				max_y = max((e*c-a*f)//(a*d-b*c),max_y)
				point.append([(b*f-e*d)//(a*d-b*c),(e*c-a*f)//(a*d-b*c)])

	result = [["."]*(abs(max_x-min_x)+1) for _ in range(abs(max_y-min_y)+1)]
	for p in point:
		row,col = p
		result[abs(col-min_y)][abs(row-min_x)] = "*"
	for i in range(len(result)):
		result[i] = ''.join(result[i])

	return result[::-1]
if __name__ == "__main__":
	print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))