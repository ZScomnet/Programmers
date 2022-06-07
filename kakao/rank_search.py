dic = dict()

def saveInfo(info, depth, data):
    if depth == 4:
        if data not in dic:
            dic[data] = []
            dic[data].append(int(info[4]))
    else:
        saveInfo(info,depth+1,data+info[depth])
        saveInfo(info,depth+1,data+"-")

def sortInfo():
    for value in dic.values():
        value.sort()

def getResult(query):
    getKey = query[0] + query[2] + query[4] + query[6]
    score = int(query[7])
    left,right = 0,len(dic[getkey])-1
    mid = (left+right) // 2
    while left<=right:
        if dic[getKey][mid] < score:
            left = mid+1
        else:
            right = mid-1
    return len(dic[getKey])-left
    
def solution(info,query):
	answer = []
    for i in info:
        saveInfo(i.split(" "),0,"")
    sortInfo()
    for q in query:
        answer.append(getResult(q.split(" ")))
    
	return answer