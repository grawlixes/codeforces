from sys import stdin, setrecursionlimit
input = stdin.readline

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache, reduce
from heapq import heappush, heappop
from math import sqrt, ceil, floor, log2

def rl(t = int):
    return tuple(map(t, input().split()))

def getNeigh(t):
    i,j = t
    return [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]

n = int(input())
p = []
ps = {}
for i in range(n):
    p.append(rl())
    ps[p[-1]] = i

#         6   
# 
#   5
# 2 1 4
#   3 
# # # # # #

# iterate
ret = [None for _ in range(n)]
seen = set()
for ot in p:
    if ot in seen:
        continue

    # get all points in this island
    island = set()
    search = set()
    search.add(ot)
    while search:
        t = search.pop()
        if t in island:
            continue
        seen.add(t)
        island.add(t)

        neigh = getNeigh(t)
        for t2 in filter(lambda t3: t3 in ps, neigh):
            search.add(t2)

    # get all coords not in points, closest to this island
    o = set()
    for t in island:
        neigh = getNeigh(t)
        for t2 in filter(lambda t3: t3 not in island, neigh):
            #print("t2", t2)
            o.add(t2)
    
    bfs = deque()
    for t in o:
        bfs.append((t, t))
    # determine the closest border point for everything on this island 
    while bfs:
        t, og = bfs.popleft()
        if t in ps and ret[ps[t]] is not None:
            continue

        if t in ps:
            ret[ps[t]] = og
        
        neigh = getNeigh(t)
        for t2 in filter(lambda t3: t3 in island, neigh):
            bfs.append((t2, og))

#print(ret)
for i,j in ret:
    print(i,j)
