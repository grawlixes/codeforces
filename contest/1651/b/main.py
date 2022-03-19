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
lim = 10**9
for t in range(1, T + 1):
    n = int(input())
    ret = [1]
    good = True
    # b - a = 2*a
    #  2  6   
    # 1, 3, 9, 27
    for i in range(n - 1):
        ret.append(ret[-1]*3)
        if ret[-1] > lim:
            good = False
            break

    if good:
        print("YES")
        print(' '.join(map(str, ret)))
    else:
        print("NO")
