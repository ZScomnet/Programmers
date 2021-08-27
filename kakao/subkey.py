from itertools import combinations

def check_invalid(combi,db):
	row = []
	
	for i in range(len(db[0])):
		line = ""
		for col in combi:
			line += str(db[col][i])
		if line in row:
			return False
		else:
			row.append(line)
	return True
	
def check_overlap(combi,result):
	li = []
	for i in range(1,len(combi)+1):
		li += list(combinations(list(combi),i))
	for l in li:
		if l in result:
			return False
	return True


def solution(relation):
	db = dict()
	com = []
	for i in range(len(relation[0])):
		db[i] = []
		com.append(i)
	for row in range(len(relation)):
		for col in range(len(relation[row])):
			db[col].append(relation[row][col])

	combi = []
	for i in range(1,len(com)+1):
		combi += list(combinations(com,i))

	result = []
	for c in combi:
		if check_invalid(c,db) and check_overlap(c,result):
			result.append(c)

	return len(result)

if __name__ == "__main__":
	print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))