# def solution(record):
# 	db = [""] * 5000000
# 	end = []
# 	for i in record:
# 		user = i.split()
# 		addr = hash(user[1]) % 5000000
# 		if user[0] == "Enter":
# 			db[addr] = user[2]
# 			end.append("Enter")
# 		elif user[0] == "Leave":
# 			end.append("Leave")
# 		else:
# 			db[addr] = user[2]
# 			end.append("X")
# 	# 최종 닉네임 정하기
# 	answer = []
# 	for addr, end in zip(record,end):
# 		if end == "Enter":
# 			answer.append(db[hash(addr.split()[1])%5000000]+"님이 들어왔습니다.")
# 		elif end == "Leave":
# 			answer.append(db[hash(addr.split()[1])%5000000]+"님이 나갔습니다.")

# 	return answer

def solution(record):
	db = dict()
	user_id = []
	end = []
	for i in record:
		user = i.split()
		if user[0] == "Enter" or user[0] == "Change":
			db[user[1]] = user[2]
		user_id.append(user[1])
		end.append(user[0])
	answer = []
	for i,e in zip(user_id,end):
		if e == "Enter":
			answer.append(db[i]+"님이 들어왔습니다.")
		elif e == "Leave":
			answer.append(db[i]+"님이 나갔습니다.")

	return answer
print(solution(["Enter 1 1", "Enter 2 2", "Change 1 2","Change 2 1","Enter 3 3","Leave 1","Leave 2","Leave 3", "Enter 1 3", "Enter 2 2"]))
