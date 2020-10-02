import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr_list = sorted(arr)
    minimum = 2*10**9
    for i in range(1, len(arr)):
        minimum = min(minimum, abs(arr_list[i - 1] - arr_list[i]))
    
    return minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
