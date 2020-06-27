#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    lastAnswer=0
    seqList=[]
    answer=[]
    for i in range(n):
        seqList.append([])
    for q,x,y in queries:
        if q==1:
            index=(x ^ lastAnswer) % n
            seqList[index].append(y)
        else:
            index=(x ^ lastAnswer) % n
            lastAnswer=seqList[index][y % len(seqList[index])]
            answer.append(lastAnswer)
    return answer
            




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
