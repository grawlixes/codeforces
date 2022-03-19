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

for t in range(1, T + 1):
    n = int(input())
    a = rl()
    b = rl()
    ret = float('inf')

    for ea1, ea2, eb1, eb2 in ((a[0], a[-1], b[0], b[-1]), (a[0], a[-1], b[-1], b[0]), (a[-1], a[0], b[0], b[-1]), (a[-1], a[0], b[-1], b[0])):
        # a - a - a - a
        # |           | 
        # b - b - b - b
        ret = min(ret, abs(ea1 - eb1) + abs(ea2 - eb2))

        # a - a - a - a
        # |         X  
        # b - b - b - b
        tra = trb = float('inf')
        for el in b:
            tra = min(tra, abs(ea2 - el))
        for el in a:
            trb = min(trb, abs(eb2 - el))
        ret = min(ret, tra + trb + abs(ea1 - eb1))

        # a - a - a - a
        #   X       X  
        # b - b - b - b
        this = tra + trb
        tra = trb = float('inf')
        for el in b:
            tra = min(tra, abs(ea1 - el))
        for el in a:
            trb = min(trb, abs(eb1 - el))
        ret = min(ret, tra + trb + this)

    print(ret)
