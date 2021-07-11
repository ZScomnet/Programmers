def collect(list_db,user_list,line):
	if len(line) == len(user_list):
		line_check = set(line)
		if line_check not in list_db and len(line_check) == len(line):
			list_db.append(set(line.copy()))
	else:
		for i in user_list[len(line)]:
			line.append(i)
			collect(list_db,user_list,line)
			line.pop()

def solution(user_id,banned_id):
	user_list = [[] for _ in range(len(banned_id))]
	for user in user_id:
		for ban,index in zip(banned_id,range(len(banned_id))):
			same_cnt = 0
			if len(user) == len(ban):
				for u,b in zip(user,ban):
					if u == b or b == '*':
						same_cnt += 1

			if same_cnt == len(ban):
				user_list[index].append(user)
	list_db = []
	collect(list_db,user_list,[])
	return len(list_db)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))