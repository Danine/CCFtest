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
    if i[0] == 0 or i[0] == 1:
        add += i[1]
    elif i[0] == 2:
        add = add + i[1] + ryg[0]
    else:
        continue
print(add)