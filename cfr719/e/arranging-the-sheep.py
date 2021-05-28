T = int(input())

for t in range(1, T + 1):
    n = int(input())
    sheep = input().strip()

    if len(set(sheep)) == 1:
        print(0)
        continue

    prev = 0
    numPrev = 0
    after = sum(i for i in range(len(sheep)) \
                  if sheep[i] == '*')
    numAfter = sheep.count('*')

    ret = float('inf')
    for i in range(len(sheep)):
        if sheep[i] == '.':
            continue
        
        after -= i
        numAfter -= 1

        costPrev = (numPrev * i) - \
                   prev - \
                   (numPrev * (numPrev + 1)) // 2
        costAfter = after - \
                    (numAfter * i) - \
                    (numAfter * (numAfter + 1)) // 2

        ret = min(ret, costPrev + costAfter)

        prev += i
        numPrev += 1

    print(ret)
