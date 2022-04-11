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

def isFeas(a, reach, days):
    ones = (days // 2) + (days % 2)
    twos = (days // 2)
    for el in a:
        d = reach - el
        tt = d // 2
        d -= min(tt, twos)*2
        twos -= min(tt, twos)
        ones -= d
        
        if ones < 0:
            return False

    return True

for t in range(1, T + 1):
    n = int(input())
    a = rl()
    a.sort()

    re = a[-1]
    ret = float('inf')
    for reach in (re, re + 1):
        
        i, j = 0, 10**15
        while i < j - 1:
            m = (i + j) // 2
            if isFeas(a, reach, m):
                j = m
            else:
                i = m + 1

        ret = min(ret, (i if isFeas(a, reach, i) else j))
    print(ret)
