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
    sn = str(n)
    p = 10**(len(sn) - 1)
    ret = []
    for el in sn:
        el = int(el)
        if el != 0:
            ret.append(p * el)
        p //= 10
    print(len(ret))
    print(' '.join(map(str, ret)))
