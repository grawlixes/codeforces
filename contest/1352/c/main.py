from sys import stdin, setrecursionlimit
input = stdin.readline

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache, reduce
from heapq import heappush, heappop
from math import sqrt, ceil, floor, log2

T = int(input())

def rl(t = int):
    return list(map(t, input().split()))

# count of numbers in [1, n] that aren't
# divisible by k
def notDivLTE(m, n):
    areDiv = m // n
    return m - areDiv

for t in range(1, T + 1):
    n, k = rl()
    i, j = 1, 10**15

    while i < j - 1:
        m = (i + j) // 2
        ct = notDivLTE(m, n)

        if ct >= k:
            j = m
        else:
            i = m + 1

    print(i if notDivLTE(i, n) == k else j)
