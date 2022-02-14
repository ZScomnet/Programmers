from itertools import permutations

def solution(user_id,banned_id):
	answer = []
	combi = list(permutations(user_id,len(banned_id)))
	for i in combi:
		is_user = True
		for user,ban in zip(i,banned_id):
			if len(user) == len(ban):
				for u,b in zip(user,ban):
					if u != b and b != '*':
						is_user = False
						break
			else:
				is_user = False
				break
			if not is_user:
				break

		if is_user:
			temp = list(i)
			temp.sort()
			temp = ''.join(temp)
			if temp not in answer:
				answer.append(temp)
	return len(answer)

if __name__ == "__main__":
	print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "abc1**"]))