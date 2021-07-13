def solution(s):
	result = ""
	num_dic = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
	char_num = ""
	for lit in s:
		if '0' <= lit <= '9':
			result += lit
		else:
			char_num += lit
		if len(char_num) == 3:
			if char_num == 'one':
				result += '1'
				char_num = ""
			elif char_num == 'two':
				result += '2'
				char_num = ""
			elif char_num == 'six':
				result += '6'
				char_num = ""
		elif len(char_num) == 4:
			if char_num == 'zero':
				result += '0'
				char_num = ""
			elif char_num == 'four':
				result += '4'
				char_num = ""
			elif char_num == 'five':
				result += '5'
				char_num = ""
			elif char_num == 'nine':
				result += '9'
				char_num = ""
		elif len(char_num) == 5:
			if char_num == 'three':
				result += '3'
				char_num = ""
			elif char_num == 'seven':
				result += '7'
				char_num = ""
			elif char_num == 'eight':
				result += '8'
				char_num = ""

	return int(result)

print(solution("23four5six7"))