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
	if num[0] > 0:
		answer += 1
	for i in range(1,k//2+1):
		if i == k/2:
			break
		answer += max(num[i],num[k-i])
	if k%2 == 0 and num[k//2] > 0:
		answer += 1
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