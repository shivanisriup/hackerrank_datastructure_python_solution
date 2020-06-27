#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def sum_list(list1):
        total = 0
        for ele in range(0, len(list1)):
            total = total + list1[ele]
        return total

def hourglassSum(arr):
    max = -1000
    s= []
    sub_array = []
    for m in range(4):
        print(m)
        for col in range(4):
            for row in range(3):
                sub_array.append(arr[row+m][col:col+3])
                s = sub_array
            hour_sum = sum_list(s[0])+s[1][1]+sum_list(s[2])
            if (max<hour_sum):
                max = hour_sum
            sub_array = []
        
    return max

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
