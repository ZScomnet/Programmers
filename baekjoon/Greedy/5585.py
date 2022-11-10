def solution():
	N = int(input())
	charge = 1000-N
	answer = 0
	for coin in [500,100,50,10,5,1]:
		if charge // coin > 0:
			answer += charge // coin
			charge -= coin * (charge // coin)

	return answer
if __name__ == "__main__":
	print(solution())