import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    sorted_list = sorted(q)
    suma = 0
    for i in range(len(q)):
        if q[i] != sorted_list[i]:
            sub = q[i] - sorted_list[i]
            if sub >= 3:
                print("too chaotic")
                suma = 0
                break
            elif sub <= 0:
                sub = 0
            else:
                suma += sub
        else:
            i = i+1
    if suma != 0: 
        print(suma)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)