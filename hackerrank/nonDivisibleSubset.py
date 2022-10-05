#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
	answer = 0
	num = [0] * k
	for i in s:
		num[i%k] += 1
	print(num)
	for i in range(k):
		if (i+i)%k == 0 and num[i] > 1:
			continue
		answer = max(num[i],answer)
		for j in range(i+1,k):
			print(i,j,answer)
			if (j+j)%k == 0:
				continue
			if (i+j)%k != 0:
				answer = max(num[i]+num[j],answer)
	return answer
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()