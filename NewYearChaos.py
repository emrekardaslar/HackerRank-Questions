#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    total = 0
    initial = []
    for i in range(len(q)):
        initial.append(i+1)
    
    for i in range(len(q)):
        if q[i] != initial[i]:
            if initial[i+1] == q[i]:
                temp = initial[i+1]
                initial[i+1] = initial[i]
                initial[i] = temp

                total+=1
            elif initial[i+2] == q[i]:
                temp = initial[i+2]
                initial[i+2] = initial[i+1]
                initial[i+1] = initial[i]
                initial[i] = temp
                
                total+=2
            else:
                print("Too chaotic")
                return
    print (total)




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
