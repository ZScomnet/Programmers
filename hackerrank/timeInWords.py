#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
	dic = {1 : "one",2 : "two", 3: "three", 4: "four", 5: "five", 6: "six",
		7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
		13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen", 17: "seventeen",
		18: "eighteen", 19: "nineteen", 20: "twenty", 30: "half"}
	for i in range(21,30):
		dic[i] = dic[20] + " " + dic[i-20]

	if m == 0:
		return dic[h] + " o' clock"
	elif m == 15 or m == 30:
		return dic[m] + " past " + dic[h]
	elif m == 45 and h < 12:
		m = 60 - m
		return dic[m] + " to " + dic[h+1]
	elif m == 45 and h == 12:
		m = 60 - m
		return dic[m] + " to " + dic[1]
	elif m == 1:
		return dic[m] + " minute past " + dic[h]
	elif m == 59 and h < 12:
		m = 60 - m
		return dic[m] + " minute to " + dic[h+1]
	elif m == 59 and h == 12:
		m = 60 - m
		return dic[m] + " minute to " + dic[1]
	elif 1 < m < 30:
		return dic[m] + " minutes past " + dic[h]
	elif 31 < m < 59:
		m = 60 - m
		return dic[m] + " minutes to " + dic[h+1]


    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
