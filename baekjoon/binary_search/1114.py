import sys
input = sys.stdin.readline

def cutTree(length,pieces,maxPiece,C):
	if length < maxPiece:
		return 1e9, 0
	cnt, total = 0,0
	for piece in pieces:
		total += piece
		if total > length:
			cnt += 1
			total = piece
	if cnt == C:
		return cnt, total
	else:
		return cnt, pieces[-1]


def solution():
	L,K,C = map(int,input().split())
	cutPoint = [0] + sorted(list(map(int,input().split()))) + [L]
	pieces = [cutPoint[i] - cutPoint[i-1] for i in range(len(cutPoint)-1,0,-1)]
	maxPiece = max(pieces)
	answerLong, answerMin = 0,0
	left,right = 0,L
	while left <= right:
		mid = (left+right) // 2
		cnt, total = cutTree(mid, pieces, maxPiece, C)
		if cnt <= C:
			answerLong = mid
			answerMin = total
			right = mid-1
		else:
			left = mid+1
	print(answerLong, answerMin)
	
if __name__ == "__main__":
	solution()