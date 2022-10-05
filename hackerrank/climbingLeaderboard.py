#!/bin/python3
from collections import deque
import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    answer = []
    ranked,player = deque(ranked),deque(player)
    new_ranked = deque()
    new_ranked.append(ranked.popleft())
    while ranked:
        if new_ranked[-1] != ranked[0]:
            new_ranked.append(ranked.popleft())
        else:
            ranked.popleft()
    ranked = new_ranked
    while player:
        score = player.popleft()
        left,right = 0,len(ranked)
        while left < right:
            mid = (left+right) // 2
            if ranked[mid] > score:
                left = mid+1
            else:
                right = mid
        answer.append(left+1)
    return answer
        
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()