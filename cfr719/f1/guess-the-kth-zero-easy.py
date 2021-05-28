n, t = map(int, input().split(' '))
for _ in range(t):
    k = int(input())
    if k == -1:
        exit(0)
    
    i, j = 1, n
    while i < j:
        m = (i + j) // 2
        print(' '.join(['?', str(i), str(m)]), flush=True)
        out = (m - i + 1) - int(input())
        
        if out >= k:
            j = m
        else:
            i = m + 1
            k -= out
            continue
            if i == m:
                i = j = i + 1
            else:
                i = m
                k -= out

    print("! " + str(i), flush=True)

