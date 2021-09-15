def search(board,row,result,line,left,right):
	if row == len(board):
		result[0] += 1
	else:
		for col in range(len(board)):
			if line[col] == 0 and right[len(board)-1-row+col] == 0 and left[col+row] == 0:
				line[col] = 1
				right[len(board)-1-row+col] = 1
				left[row+col] = 1
				search(board,row+1,result,line,left,right)
				line[col] = 0
				right[len(board)-1-row+col] = 0
				left[row+col] = 0


def Nqueen(N):
	board = [[0]*N for _ in range(N)]
	result = [0]
	line,left,right = [0]*N,[0]*(2*N-1),[0]*(2*N-1)
	search(board,0,result,line,left,right)
	return result[0]

if __name__ == "__main__":
	print(Nqueen(int(input())))
