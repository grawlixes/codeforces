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


    prev = moves = 0
    ab = [0, 0]
    ij = [0, n - 1]
    turn = 0
    while ij[0] <= ij[1]:
        eaten = 0
        while True:
            ci = ij[turn]
            ab[turn] += a[ci]
            eaten += a[ci]

            add = [1, -1][turn]
            ij[turn] += add
            if ij[0] > ij[1] or eaten > prev:
                break
        
        #print("after move", moves+1, eaten, ab, ij)
        prev = eaten
        turn = 1 - turn
        moves += 1

    print(' '.join(map(str, [moves] + ab)))
