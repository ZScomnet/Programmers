def solution(length,price):
	answer = 0
	now = price[0]
	finish = 0
	for i in range(len(price)):
		if now > price[i]:
			answer += finish*now
			now = price[i]
			finish = 0
		finish += length[i]
	if finish != 0:
		answer += now * finish
	return answer

if __name__ == "__main__":
	N = int(input())
	length = list(map(int,input().split()))
	price = list(map(int,input().split()))
	print(solution(length,price[:-1]))