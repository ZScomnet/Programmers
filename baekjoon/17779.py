import sys
input = sys.stdin.readline

def find_divide(N,board,row,col):
	half = []
	result = []
	for d1 in range(1,N//2+1):
		if 0 <= row+d1 < N and 0 <= col-d1 < N:
			half.append([row+d1,col-d1])
		else:
			break
	for d2 in range(1,N//2+1):
		for i in half:
			r,c = i
			if 0 <= row+d2 < N and 0 <= col+d2 < N and 0 <= r+d2 < N and 0 <= c+d2 < N:
				result.append([(row,col),(r,c),(row+d2,col+d2),(r+d2,c+d2)])
			else:
				break
	return result 

def city1(N,board,u,l):
	people = 0
	end = u[1]
	for row in range(l[0]):
		if row >= u[0]:
			end -= 1
		for col in range(end+1):
			people += board[row][col]
	return people

def city2(N,board,u,r):
	people = 0
	start = u[1]+1
	for row in range(r[0]+1):
		if row > u[0]:
			start += 1
		for col in range(start,N):
			people += board[row][col]
	return people

def city3(N,board,d,r):
	people = 0
	start = r[1]
	for row in range(r[0]+1,N):
		for col in range(start,N):
			people += board[row][col]
		if start != d[1]:
			start -= 1
	return people

def city4(N,board,d,l):
	people = 0
	end = l[1]
	for row in range(l[0],N):
		for col in range(end):
			people += board[row][col]
		if end < d[1]:
			end += 1
	return people

def solution(N,board):
	divide = []
	for row in range(N):
		for col in range(1,N):
			divide += find_divide(N,board,row,col)

	people = 0
	for i in board:
		people += sum(i)

	answer = people
	for i in divide:
		u,l,r,d = i
		
		max_p,min_p = 0,1e9
		p1 = city1(N,board,u,l)
		max_p = max(p1,max_p)
		min_p = min(p1,min_p)
		p2 = city2(N,board,u,r)
		max_p = max(p2,max_p)
		min_p = min(p2,min_p)
		p3 = city3(N,board,d,r)
		max_p = max(p3,max_p)
		min_p = min(p3,min_p)
		p4 = city4(N,board,d,l)
		max_p = max(p4,max_p)
		min_p = min(p4,min_p)
		p5 = people - (p1+p2+p3+p4)
		max_p = max(p5,max_p)
		min_p = min(p5,min_p)
		answer = min(answer,max_p-min_p)
	return answer

if __name__ == "__main__":
	N = int(input())
	board = []
	for _ in range(N):
		board.append(list(map(int,input().split())))
	print(solution(N,board))