#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    for row in range(len(G)-len(P)+1):
        for col in range(len(G[0])-len(P[0])+1):
            if G[row][col] == P[0][0]:
                isGrid = True
                for r in range(len(P)):
                    for c in range(len(P[0])):
                        if G[row+r][col+c] != P[r][c]:
                            isGrid = False
                            break
                    if not isGrid:
                        break
                if isGrid:
                    return "YES"
    return "NO"
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()