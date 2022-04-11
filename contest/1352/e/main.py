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
    ct = {}
    for el in a:
        ct[el] = ct.get(el, 0) + 1

    ret = 0
    for i in range(n):
        s = a[i]
        for j in range(i + 1, n):
            s += a[j]
            if s > n:
                break
            
            if s in ct:
                ret += ct[s]
                del ct[s]
    
    print(ret)
