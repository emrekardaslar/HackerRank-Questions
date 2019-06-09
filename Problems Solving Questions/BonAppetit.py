#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def annapays(bill,k):
    anna = 0
    for i in range(len(bill)):
        if i != k:
            anna += bill[i]
    return anna / 2

def brianpays(bill):
    brian = 0
    for i in range(len(bill)):
        brian += bill[i]
    return brian / 2


def bonAppetit(bill, k, b):
    brian = brianpays(bill)
    anna = annapays(bill,k)
    if b == anna:
        print("Bon Appetit")
    else:
        result = int ((brian - anna))
        print(result)



if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
