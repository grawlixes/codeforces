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
    if n < 4:
        print(-1)
        continue

    diff = [2, -3, 2, 3]
    i = 0
    ret = [2]
    lim = (n // 4) * 4
    while len(ret) < lim:
        ret.append(ret[-1] + diff[i])
        i = (i + 1) % 4

    mod = n % 4
    if mod == 0:
        pass
    elif mod == 1:
        ret.append(n)
    elif mod == 2:
        last = ret.pop()
        ret.append(n-1)
        ret.append(last)
        ret.append(n)
    else:
        # 2 4 1 3 5 6 7
        # 2 4 1 5 7 3 6   
        last = ret.pop()
        ret.append(n-2)
        ret.append(n)
        ret.append(last)
        ret.append(n-1)

    print(' '.join(map(str, ret)))
    # 2, 4, 1, 3, 5
