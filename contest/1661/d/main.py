from sys import stdin, setrecursionlimit
input = stdin.readline

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache, reduce
from heapq import heappush, heappop
from math import sqrt, ceil, floor, log2


def rl(t = int):
    return list(map(t, input().split()))

n, k = rl()
b = rl()
carry = 0
ret = 0
lastK = 0
d = deque()
# [2, 0,  
# carry = 2
# lastK = 2
for i in range(n - 1, -1, -1):
    #print(b[i], carry, ret)
    need = max(0, b[i] - carry)
    #print(need)
    val = min(k, i+1)
    add = ceil(need / val)
    ret += add
    
    d.append(add)
    if len(d) > k:
        lastK -= d.popleft()
    carry += (val - 1) * add
    carry -= lastK
    
    lastK += add

print(ret)
