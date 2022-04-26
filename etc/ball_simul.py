# from collections import deque

# d = [(0,1),(0,-1),(1,0),(-1,0)]

# def check(way,row,col,n,m):
# 	if way == 0 and col == 0:
# 		return False
# 	elif way == 1 and col == m-1:
# 		return False
# 	elif way == 2 and row == 0:
# 		return False
# 	elif way == 3 and row == n-1:
# 		return False
# 	else:
# 		return True

# def solution(n,m,x,y,queries):
# 	q = deque()
# 	q.append([x,y])
# 	while queries:
# 		way,length = queries.pop()
# 		next_q = deque()
# 		print(q)
# 		while q:
# 			row,col = q.popleft()
# 			dr,dc = d[way]
# 			if check(way,row,col,n,m):
# 				row += dr*length
# 				col += dc*length
# 				if 0 <= row < n and 0 <= col < m:
# 					next_q.append([row,col])
# 			else:
# 				for i in range(length+1):
# 					if 0 <= row+dr*i < n and 0 <= col+dc*i < m:
# 						next_q.append([row+dr*i,col+dc*i])
# 					else:
# 						break
# 		q = next_q

# 	return len(q)

d = [(0,1),(0,-1),(1,0),(-1,0)]

def check(way,row,col,n,m):
	if way == 0 and col == 0:
		return False
	elif way == 1 and col == m-1:
		return False
	elif way == 2 and row == 0:
		return False
	elif way == 3 and row == n-1:
		return False
	else:
		return True

def move(n,m,lu,rd,dr,dc,length):
	lu[0],lu[1] = lu[0]+dr*length, lu[1]+dc*length
	rd[0],rd[1] = rd[0]+dr*length, rd[1]+dc*length

	if ((lu[0] < 0 or lu[0] >= n) and (rd[0] < 0 or rd[0] >= n)) or ((lu[1] < 0 or lu[1] >= m) and (rd[1] < 0 or rd[1] >= m)):
		return True

	lu[0],lu[1] = min(lu[0],n-1),min(lu[1],m-1)
	lu[0],lu[1] = max(lu[0],0),max(lu[1],0)

	rd[0],rd[1] = min(rd[0],n-1),min(rd[1],m-1)
	rd[0],rd[1] = max(rd[0],0),max(rd[1],0)
	return False

def solution(n,m,x,y,queries):
	lu,rd = [x,y],[x,y]
	while queries:
		# print(lu,ru)
		# print(ld,rd)
		# print()
		way,length = queries.pop()
		dr,dc = d[way]
		if way == 0 or way == 2:
			if check(way,lu[0],lu[1],n,m):
				# print(i)
				if move(n,m,lu,rd,dr,dc,length):
					return 0
			else:
				if way == 0:
					rd[1] += length
					rd[1] = min(rd[1],m-1)
				else:
					rd[0] += length
					rd[0] = min(rd[0],n-1)
		else:
			if check(way,rd[0],rd[1],n,m):
				# print(i)
				if move(n,m,lu,rd,dr,dc,length):
					return 0
			else:
				if way == 1:
					lu[1] -= length
					lu[1] = max(lu[1],0)
				else:
					lu[0] -= length
					lu[0] = max(lu[0],0)
	return (rd[0]-lu[0]+1) * (rd[1]-lu[1]+1)

if __name__ == '__main__':
	print(solution(5,5,2,2,[[1,100]]))

# 0 : left , 1 : right ,  2 : up , 3 : down