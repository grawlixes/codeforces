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

    @lru_cache(None)
    def dfs(i = 0, swappedLast = False):
        if i == n:
            return 0
        
        ret = float('inf')
        if swappedLast:
            ret = dfs(i + 1, False) + (0 if i == 0 else (abs(a[i] - b[i-1]) + abs(b[i] - a[i-1])))
            swap = dfs(i + 1, True) + (0 if i == 0 else (abs(b[i] - b[i-1]) + abs(a[i] - a[i-1])))
            ret = min(ret, swap)
        else:
            ret = dfs(i + 1, True) + (0 if i == 0 else (abs(a[i] - b[i-1]) + abs(b[i] - a[i-1])))
            swap = dfs(i + 1, False) + (0 if i == 0 else (abs(b[i] - b[i-1]) + abs(a[i] - a[i-1])))
            ret = min(ret, swap)

        return ret

    print(dfs())
