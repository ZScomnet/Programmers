# import sys
# sys.setrecursionlimit(100001)
# def divide(now,n):
# 	if now == n:
# 		return 1
# 	elif now == n-1:
# 		return 1
# 	else:
# 		return divide(now+1,n) + divide(now+2,n)

def solution(n):
#	return divide(0,n)
    before,tile = 0,1
    for i in range(n):
        before,tile = tile,before + tile
    return tile % 1000000007