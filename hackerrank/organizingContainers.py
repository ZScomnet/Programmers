#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    size = [0]*len(container)
    ball = [0]*len(container)
    for row in range(len(container)):
        for col in range(len(container)):
            size[row] += container[row][col]
            ball[col] += container[row][col]
    for i in range(len(size)):
        for j in range(len(ball)):
            if size[i] == ball[j] and size[i] != -1 and ball[j] != -1:
                size[i] = -1
                ball[j] = -1
                break
        if size[i] != -1:
            return "Impossible"

    return "Possible"
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()
