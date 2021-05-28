T = int(input())
NUMS = sorted(set(int(str(i) * j) for i in range(1, 9 + 1) for j in range(1, 9 + 1)))

from bisect import bisect_right
for t in range(1, T + 1):
    n = int(input())
    print(bisect_right(NUMS, n)) 
