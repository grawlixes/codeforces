from sys import stdin, setrecursionlimit
input = stdin.readline

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache, reduce
from heapq import heappush, heappop
from math import sqrt, ceil, floor, log2

def rl(t = int):
    return list(map(t, input().split()))

n = rl()
b = []
for _ in range(3):
    b.append(input().strip())
q = int(input())
queries = []
for _ in range(q):
    queries.append(rl())


