def search(tree,cost,now,money):
	if now == '-':
		cost[now] += money

	elif money // 10 > 0:
		cost[now] += money-(money//10)
		search(tree,cost,tree[now],money//10)

	else:
		cost[now] += money

def solution(enroll,referral,seller,amount):
	tree = dict()
	cost = dict()
	tree['-'] = '-'
	cost['-'] = 0
	for i,j in zip(enroll,referral):
		tree[i] = j
		cost[i] = 0

	for s,a in zip(seller,amount):
		search(tree,cost,s,a*100)

	return list(cost.values())[1:]

if __name__ == "__main__":
	print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))