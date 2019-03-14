n = int(input())
temp = input()
fst = [int(i) for i in temp.split()]
scd = []
for bus in range(n):
    if bus == 0:
        price = (fst[bus] + fst[bus+1])/2
        scd.append(int(price))
    elif bus == n-1:
        price = (fst[bus-1] + fst[bus])/2
        scd.append(int(price))
    else:
        price = (fst[bus-1] + fst[bus] + fst[bus+1])/3
        scd.append(int(price))
for i in scd:
    print(i,end = ' ')