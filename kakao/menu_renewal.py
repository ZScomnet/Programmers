def mini_course(c,order,size,db):
	if len(c) == size:
		db.append(c)
	else:
		for lit in range(len(order)):
			erase = c
			c += order[lit]
			mini_course(c,order[lit+1:],size,db)
			c = erase

def solution(orders,course):
	answer = []
	length = 2
	while length < 11:
		dic = dict()
		if length in course:
			for order in orders:
				menu = []
				for i in order:
					menu.append(i)
				menu = sorted(menu)
				db = []
				mini_course("",menu,length,db)
				for i in db:
					if i in dic:
						dic[i] += 1
					else:
						dic[i] = 1
			size = 0
			max_course = []
			for key,value in zip(dic.keys(),dic.values()):
				if size < value:
					max_course = [key]
					size = value
				elif size == value:
					max_course.append(key)
			if size != 1:
				answer += max_course

		length += 1
	answer.sort()

	return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
