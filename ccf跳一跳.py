temp = input()
steps = [int(n) for n in temp.split()]

center = False
point = 0; total = 0
for i in steps:
    if i == 1:
        total += 1
        point = 0
        center = False
    elif i == 2:
        if center:
            point += 2
            total += point
            center = True
        else:
            point = 2
            total += point
            center = True
    else:
        break

print(total)
