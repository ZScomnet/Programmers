#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
	q = []
	start = -1
	answer = ""
	for i in range(len(w)):
		if i == len(w)-1 and start != -1:
			heapq.heappush(q,w[i])
		elif i == len(w)-1 and start == -1:
			break
		elif ord(w[i]) < ord(w[i+1]):
			start = i
			q = []
			heapq.heappush(q,w[i])
		elif start != -1:
			heapq.heappush(q,w[i])

	if start == -1:
		return "no answer"
	else:
		second = True
		for i in range(len(w)):
			if len(q) == 0:
				break
			if i < start:
				answer += w[i]
			else:
				if second:
					s = ""
					while second:
						if ord(w[i]) >= ord(q[0]):
							s += heapq.heappop(q)
						else:
							answer += heapq.heappop(q)
							answer += s
							second = False
				else:
					answer += heapq.heappop(q)
	return answer


	# Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
