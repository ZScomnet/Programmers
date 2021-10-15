import sys

input = sys.stdin.readline

def divide(board,row,col,length):
	if length == 1:
		return board[row][col]
	else:
		lu = divide(board,row,col,length//2)
		ru = divide(board,row,col+int(length/2),length//2)
		ld = divide(board,row+int(length/2),col,length//2)
		rd = divide(board,row+int(length/2),col+int(length/2),length//2)
		if lu == ru == ld == rd == 1 or lu == ru == ld == rd == 0:
			return lu
		else:
			return "(" + str(lu) + str(ru) + str(ld) + str(rd) + ")"
def solution(board):
	return divide(board,0,0,len(board))

if __name__ == "__main__":
	N = int(input())
	board = []
	for _ in range(N):
		line = []
		l = input()
		for i in range(N):
			line.append(int(l[i]))
		board.append(line)
	print(solution(board))