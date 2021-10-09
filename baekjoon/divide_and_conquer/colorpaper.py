import sys
input = sys.stdin.readline

def paper(board,row,col,length,answer):
	if length == 1:
		return board[row][col]
	else:
		lu = paper(board,row,col,int(length/2),answer)
		ld = paper(board,row+int(length/2),col,int(length/2),answer)
		ru = paper(board,row,col+int(length/2),int(length/2),answer)
		rd = paper(board,row+int(length/2),col+int(length/2),int(length/2),answer)
		if lu == ld == ru == rd == 1:
			return 1
		elif lu == ld == ru == rd == 0:
			return 0
		else:
			if lu == 1:
				answer[1] += 1
			elif lu == 0:
				answer[0] += 1
			if ld == 1:
				answer[1] += 1
			elif ld == 0:
				answer[0] += 1
			if ru == 1:
				answer[1] += 1
			elif ru == 0:
				answer[0] += 1
			if rd == 1:
				answer[1] += 1
			elif rd == 0:
				answer[0] += 1
	return answer


def solution(board):
	answer = [0,0]
	answer = paper(board,0,0,len(board),answer)
	if answer == 1:
		print(0)
		print(1)
	elif answer == 0:
		print(1)
		print(0)
	else:
		print(answer[0])
		print(answer[1])

if __name__ == "__main__":
	N = int(input())
	board = []
	for _ in range(N):
		line = list(map(int,input().split()))
		board.append(line)
	solution(board)