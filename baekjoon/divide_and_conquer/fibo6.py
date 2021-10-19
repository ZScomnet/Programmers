# def docagne(n,db):
# 	if n <= 2:
# 		return 1
# 	else:
# 		if n <= 100000:
# 			if db[n] != 0:
# 				return db[n]
# 			elif n%2 == 0:
# 				db[n] = (docagne(n//2-1,db)*docagne(n//2,db) + docagne(n//2,db)*docagne(n//2+1,db)) % 1000000007
# 			else:
# 				db[n] = (docagne(n//2,db)*docagne(n//2,db) + docagne(n//2+1,db)*docagne(n//2+1,db)) % 1000000007
# 			return db[n]
# 		else:
# 			if n%2 == 0:
# 				return (docagne(n//2-1,db)*docagne(n//2,db) + docagne(n//2,db)*docagne(n//2+1,db)) % 1000000007
# 			else:
# 				return (docagne(n//2,db)*docagne(n//2,db) + docagne(n//2+1,db)*docagne(n//2+1,db)) % 1000000007

def multi_matrix(A,B):
	return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%1000000007,(A[0][0]*B[0][1]+A[0][1]*B[1][1])%1000000007]
	,[(A[1][0]*B[0][0]+A[1][1]*B[1][0])%1000000007,(A[1][0]*B[0][1]+A[1][1]*B[1][1])%1000000007]]

def divide(N):
	q = []
	matrix = [[1,1],[1,0]]
	while N > 1:
		if N%2 != 0:
			q.append(matrix)
		matrix = multi_matrix(matrix,matrix)
		N = N // 2
	for m in q:
		matrix = multi_matrix(matrix,m)
	print(matrix)
	return matrix[1][0]


def solution(N):
	# db = [0]*100001
	# db[1],db[2] = 1,1
	# return docagne(N,db)
	result = divide(N)
	return result
if __name__ == "__main__":
	N = int(input())
	print(solution(N))