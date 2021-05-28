T = int(input())

for t in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split(' ')))

    m = {}
    ret = 0
    for i,el in enumerate(a):
        ret += m.get(el - i, 0)
        m[el - i] = m.get(el - i, 0) + 1

    print(ret)
