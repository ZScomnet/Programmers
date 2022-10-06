#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
	answer = 0
	move = [[0,0,0],[0,0,0],[0,0,0]]
	move[0][0] = min(r_q-1,c_q-1)
	move[0][1] = r_q-1
	move[0][2] = min(r_q-1,n-c_q)
	move[1][0] = c_q-1
	move[1][2] = n-c_q
	move[2][0] = min(n-r_q,c_q-1)
	move[2][1] = n-r_q
	move[2][2] = min(n-r_q,n-c_q)

	for obstacle in obstacles:
		row,col = obstacle
		if abs(row-r_q) == abs(col-c_q):
			if row > r_q and col > c_q:
				move[2][2] = min(move[2][2],row-r_q-1)
			elif row > r_q and col < c_q:
				move[2][0] = min(move[2][0],row-r_q-1)
			elif row < r_q and col > c_q:
				move[0][2] = min(move[0][2],col-c_q-1)
			else:
				move[0][0] = min(move[0][0],c_q-col-1)
		elif abs(row-r_q) == 0:
			if col > c_q:
				move[1][2] = min(move[1][2],col-c_q-1)
			else:
				move[1][0] = min(move[1][0],c_q-col-1)
		elif abs(col-c_q) == 0:
			if row > r_q:
				move[2][1] = min(move[2][1],row-r_q-1)
			else:
				move[0][1] = min(move[0][1],r_q-row-1)
	for i in move:
		answer += sum(i)
	return answer
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
