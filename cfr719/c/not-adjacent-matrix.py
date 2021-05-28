T = int(input())

for t in range(1, T + 1):
    n = int(input())

    if n <= 2:
        print([1, -1][n - 1])
        continue
    
    ret = [[0 for _ in range(n)] for _ in range(n)]

    ret[-1][-1] = 1
    ret[-1][-2] = 8
    ret[-1][-3] = 5
    ret[-2][-1] = 4
    ret[-2][-2] = 6
    ret[-2][-3] = 3
    ret[-3][-1] = 2
    ret[-3][-2] = 9
    ret[-3][-3] = 7

    sq = 10
    for it in range(4, n + 1):
        j = -it
        while j != 0:
            ret[-it][j] = sq
            sq += 2
            j += 1
        
        i = -(it - 1)
        sq -= 3
        while i != 0:
            ret[i][-it] = sq
            sq -= 2
            i += 1

        sq = it**2 + 1

    for line in ret:
        print(' '.join(str(el) for el in line))
