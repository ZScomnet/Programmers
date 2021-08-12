def solution(sticker):
	if len(sticker)<=3:
		return max(sticker)
	else:
		memorization = [0 for _ in range(len(sticker))]
		# pull 0
		memorization[0] = sticker[0]
		memorization[1] = sticker[0]
		for i in range(2,len(memorization)-1):
			memorization[i] = max(memorization[i-1],memorization[i-2]+sticker[i])
		result_0 = max(memorization)
		# pull 1
		memorization = [0 for _ in range(len(sticker))]
		memorization[1] = sticker[1]
		for i in range(2,len(memorization)):
			memorization[i] = max(memorization[i-1],memorization[i-2]+sticker[i])
		result_1 = max(memorization)
	return max(result_0,result_1)

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))