def solution(N,number):
	answer = 0
	result = dict()
	li = [N,N+N,N-N,N*N,N//N,11*N,111*N,1111*N,11111*N,111111*N]
	cnt = [1,2,2,2,2,2,3,4,5,6]
	for i,j in zip(li,cnt):
		result[i] = j
	for i in range(8):
		next_dict = result.copy()
		# print(i)
		# for k,v in zip(result.keys(),result.values()):
		# 	print(k,v)
		for k,v in zip(result.keys(),result.values()):
			for l in li:
				if k+l in result and v+result[l] < 9:	
					next_dict[k+l] = min(v+result[l],next_dict[k+l])
				elif v+result[l] < 9:
					next_dict[k+l] = v+result[l]

				if k-l in result and k-l >= 1 and v+result[l] < 9:
					next_dict[k-l] = min(v+result[l],next_dict[k-l])
				elif k-l not in result and k-l >= 1 and v+result[l] < 9:
					next_dict[k-l] = v+result[l]

				if k*l in result and v+result[l] < 9:
					next_dict[k*l] = min(v+result[l],next_dict[k*l])
				elif v+result[l] < 9:
					next_dict[k*l] = v+result[l]

				if l != 0:
					if k//l in result and v+result[l] < 9:
						next_dict[k//l] = min(v+result[l],next_dict[k//l])
					elif v+result[l] < 9:
						next_dict[k//l] = v+result[l]
		result = next_dict
	if number not in result:
		return -1
	else:
		return result[number]

if __name__ == "__main__":
	print(solution(5,31168))