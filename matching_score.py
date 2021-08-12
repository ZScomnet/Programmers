def solution(word,pages):
	pages_name = dict()
	pages_body = []
	pages_score_dict = dict()
	for page in pages:
		all_line = page.split('\n')
		pages_name[all_line[3].split("\"")[-2]] = []
		pages_score_dict[all_line[3].split("\"")[-2]] = 0 
		body = []
		for line in range(6,len(all_line)):
			if all_line[line] == "</body>":
				break
			body.append(all_line[line])
		pages_body.append(body)

	for page_body,site in zip(pages_body,pages_name.keys()):
		score = 0
		for line in page_body:
			line_word = line.split()
			for w in line_word:
				if w[0:4] == "href":
					pages_name[site].append(w.split('\"')[1])
				w_score = 0	
				for find in range(0,len(w),len(word)):
					if w[find:find+len(word)].upper() == word.upper():
						score += 1
				if len(w) % len(word) == 0:
					score += w_score
		pages_score_dict[site] += score
	
	link_score = dict()
	for site in pages_name.keys():
		link_score[site] = 0
	print(pages_name)
	print(link_score)
	for site,link in zip(pages_name.keys(),pages_name.values()):
		try:
			for l in link:
				link_score[l] += pages_score_dict[site] / len(pages_name[site])
		except KeyError:
			pass
	result = 0
	index = 0
	answer = 0
	for score,link in zip(pages_score_dict.values(),link_score.values()):
		if result < score+link:
			result = score+link
			answer = index
		index += 1
	return answer

print(solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))