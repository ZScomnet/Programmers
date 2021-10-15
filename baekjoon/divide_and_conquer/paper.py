import sys
input = sys.stdin.readline

def cutting(board,row,col,paper,length):
	if length == 1:
		return board[row][col]
	else:
		lu = cutting(board,row,col,paper,length//3)
		mu = cutting(board,row,col+length//3,paper,length//3)
		ru = cutting(board,row,col+(length//3)*2,paper,length//3)
		lm = cutting(board,row+length//3,col,paper,length//3)
		mm = cutting(board,row+length//3,col+length//3,paper,length//3)
		rm = cutting(board,row+length//3,col+(length//3)*2,paper,length//3)
		ld = cutting(board,row+(length//3)*2,col,paper,length//3)
		md = cutting(board,row+(length//3)*2,col+length//3,paper,length//3)
		rd = cutting(board,row+(length//3)*2,col+(length//3)*2,paper,length//3)
		if lu == mu == ru == lm == mm == rm == ld == md == rd:
			return lu
		else:
			for i in [lu,mu,ru,lm,mm,rm,ld,md,rd]:
				if i == -1:
					paper[0] += 1
				elif i == 0:
					paper[1] += 1
				elif i == 1:
					paper[2] += 1
	return paper


def solution(board):
	paper = [0,0,0]
	if len(board) == 1:
		if board[0][0] == -1:
			paper[0] += 1
		else:
			paper[board[0][0]+1] += 1
	else:
		result = cutting(board,0,0,paper,len(board))
		if result == -1:
			paper[0] += 1
		elif result == 0 or result == 1:
			paper[result+1] += 1
		else:
			paper = result

	print(paper[0])
	print(paper[1])
	print(paper[2])

if __name__ == "__main__":
	N = int(input())
	board = []
	for _ in range(N):
		board.append(list(map(int,input().split())))
	solution(board)