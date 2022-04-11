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
    n, k = rl()
    if n < k:
        print("NO")
        continue

    ret = [1 for _ in range(k-1)]
    ret.append(n - (k - 1))
    if ret[-1] % 2 != 1:
        ret = [2 for _ in range(k-1)]
        ret.append(n - 2*(k-1))
        if ret[-1] <= 0 or ret[-1] % 2 == 1:
            ret = []

    if ret:
        print("YES")
        print(' '.join(map(str, ret)))
    else:
        print("NO")
