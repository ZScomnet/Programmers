def solution(enroll,referral,seller,amount):
	my_boss = dict()
	my_sell = dict()
	result = []
	for en,re in zip(enroll,referral):
		my_boss[en] = re
		my_sell[en] = 0
	for sell,am in zip(seller,amount):
		my_boss_sell = round(am*100 * 1/10)
		my_boss_name = my_boss[sell]
		my_sell[sell] += am*100 - my_boss_sell
		while my_boss_name != '-':
			my_sell[my_boss_name] += my_boss_sell - round(my_boss_sell*1/10)
			my_boss_sell = round(my_boss_sell*1/10)
			my_boss_name = my_boss[my_boss_name] 
			if my_boss_sell == 0:
				break
	for i in my_sell.values():
		result.append(i)

	return result

print(solution(["A","B","C","D","E","F","G"],["-", "A", "B","C","D","E","F"],["G","F"],[10,9]))