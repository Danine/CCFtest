rygin = input()
ryg = [int(n) for n in rygin.split()]
n = int(input())
count = []
for i in range(n):
    active = input()
    temp = [int(m) for m in active.split()]
    count.append(temp.copy())
add = 0
for i in count:
    tp = add % sum(ryg)
    if i[0] == 0:
        add += i[1]
    elif i[0] == 1:
        if 0 < tp - i[1] < ryg[2]:
            continue
        else:
            add = add + tp - i[1]
    elif i[0] == 2:
        if 0 < ryg[0]-(tp-i[1]) < ryg[0]:
            add = add + ryg[0]-(tp-i[1])
        else:
            continue
    else:
        if ryg[0] + ryg[1]-(tp-i[1]) > 0:
            add = add + ryg[0] + ryg[1]-(tp-i[1])
        else:
            continue
print(add)