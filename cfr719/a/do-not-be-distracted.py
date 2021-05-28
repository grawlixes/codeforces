T = int(input())

for t in range(1, T + 1):
    n = int(input())
    s = input().strip()

    solved = set()
    cur = None
    sus = False
    for el in s:
        if el == cur:
            continue
        else:
            solved.add(cur)
            if el in solved:
                sus = True
            cur = el

    print("NO" if sus else "YES")
