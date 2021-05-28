from heapq import heappush, heappop
from collections import deque

n, m, w = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip().split())))

# find the best teleporter to move about from
tps = set((i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] not in (0, -1))
bfs = deque([(0, 0, 0)])
tpCosts = {} 
visited = set()
minTpCost = float('inf')
while bfs:
    i, j, c = bfs.popleft()
    key = (i, j)
    if grid[i][j] == -1 or \
       key in visited:
        continue
    visited.add(key)
    
    if key in tps:
        tpCosts[key] = c
        if c + grid[i][j] < minTpCost:
            minTpCost = c + grid[i][j]

    cand = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
    
    for i2, j2 in filter(lambda tup: min(tup) >= 0 and tup[0] < n and tup[1] < m, cand):
        bfs.append((i2, j2, c + w))

print("heap time")
heap = [(0, 0, 0)]

for tp in tps:
    i, j = tp
    curCost = tpCosts.get(tp, float('inf'))
    tpCosts[tp] = min(curCost, minTpCost + \
                               grid[i][j])
    heappush(heap, (tpCosts[tp], i, j))

seen = set()
succ = False
while heap:
    t, i, j = heappop(heap)
    if t == float('inf'):
        break
    key = (i, j)
    if key == (n - 1, m - 1):
        succ = True
        print(t)
        break
    if grid[i][j] == -1 or key in seen:
        continue
    seen.add(key)
    
    cand = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
    
    for i2, j2 in filter(lambda tup: min(tup) >= 0 and tup[0] < n and tup[1] < m, cand):
        heappush(heap, (t + w, i2, j2))

if not succ:
    print(-1)

