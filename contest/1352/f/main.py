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
    ns = rl()
    if sum(ns) == ns[0]:
        print(''.join('0' for _ in range(ns[0]+1)))
        continue

    # 1 3 0
    # 1111110100
    ret = ['1']
    while ns[2]:
        ret.append('1')
        ns[2] -= 1

    if ns[0]:
        ret.append('0')
        ns[1] -= 1
        while ns[0]:
            ret.append('0')
            ns[0] -= 1

    while ns[1]:
        ret.append(str(1 - int(ret[-1])))
        ns[1] -= 1

    print(''.join(ret))
