from sys import stdin, setrecursionlimit
input = stdin.readline

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache, reduce
from heapq import heappush, heappop
from math import sqrt, ceil, floor, log2

def rl(t = int):
    return list(map(t, input().split()))

MOD = 32768
cache = {}
bfs = deque()
bfs.append((0, 0))
while bfs:
    cur, ct = bfs.popleft()
    if cur in cache:
        continue
    cache[cur] = ct

    # minus 1
    bfs.append(((cur - 1) % MOD, ct + 1))
    # div two
    if cur % 2 == 0 and cur != 0:
        bfs.append((cur // 2, ct + 1))
    # div two, over
    if cur % 2 == 0:
        bfs.append(((cur + MOD) // 2, ct + 1))

n = int(input())
a = rl()

print(' '.join(map(str, (cache[el] for el in a))))
