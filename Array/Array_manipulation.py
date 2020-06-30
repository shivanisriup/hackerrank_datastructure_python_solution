#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    list=[0]*(n+1)
    for a,b,k in queries:
        list[a]+=k
        if b + 1 <= n:
            list[b + 1] -= k
    max_sum = 0
    s = 0
    for i in list:
        s += i
        max_sum = max(max_sum, s)
    return (max_sum)
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
