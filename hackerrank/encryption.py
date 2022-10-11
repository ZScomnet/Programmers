import math
import os
import random
import re
import sys

def encryption(s):
	col = 0,0
	if len(s)**(1/2) == int(len(s)**(1/2)):
		col = int(len(s)**(1/2))
	else:
		col = int(len(s)**(1/2)) + 1

	answer = ""
	for i in range(col):
		idx = i
		string = ""
		while idx < len(s):
			string += s[idx]
			idx += col
		answer += string + " "

	return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
