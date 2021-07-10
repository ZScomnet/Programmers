# def solution(s):
# 	answer = len(s)
# 	for size in range(1,int(len(s)/2)+1):
# 		for start in range(0,size):
# 			cnt = 0
# 			result = start
# 			before = s[start:start+size]
# 			for lit in range(start,len(s),size):
# 				if before == s[lit:lit+size]:
# 					cnt += 1
# 				else:
# 					if cnt == 1:
# 						result += size
# 					else:
# 						result += size+1
# 						cnt = 1
# 					before = s[lit:lit+size]
# 			if cnt != 1:
# 				result += size+1
# 			elif cnt == 1 and (len(s)-start)%size == 0:
# 				result += size
# 			else:
# 				result += (len(s)-start)%size
# 			print(start,size,result)
# 			if result < answer:
# 				answer = result

# 	return answer

def solution(s):
	answer = len(s)
	for size in range(1,int(len(s)/2)+1):
		cnt = 0
		result = ""
		before = s[0:size]
		for lit in range(0,len(s),size):
			if before == s[lit:lit+size]:
				cnt += 1
			else:
				if cnt == 1:
					result += before
				else:
					result += str(cnt)
					result += before
					cnt = 1
				before = s[lit:lit+size]
			print(size,result)
		
		if (len(s)%size) != 0 and cnt == 1:
			result += s[-(len(s)%size):]
		elif cnt != 1:
			result += str(cnt) + s[-size:]
		else:
			result += s[-size:]
		if answer > len(result):
			answer = len(result)
	return answer

print(solution("abcabcdede"))