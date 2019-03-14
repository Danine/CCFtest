n = int(input())
xh = []
xw = []

for i in range(n):
    temp = input()
    time = [int(j) for j in temp.split()]
    time[1] -= 1
    xh.append(time.copy())

for i in range(n):
    temp = input()
    time = [int(j) for j in temp.split()]
    time[1] -= 1
    xw.append(time.copy())

line = []
for i in range(max(xh[-1][1],xw[-1][1])+1):
    line.append(0)

for i in xh:
    for j in range(i[0],i[1]+1):
        line[j] = 1

for i in xw:
    for j in range(i[0],i[1]+1):
   
        if line[j] == 1:
            line[j] = 2

print(line.count(2))



# h = 0; w = 0
# chat = 0
# while(h < n and w < n):
#     if xh[h][0] in range(xw[w][0],xw[w][1]+1):
#         if xh[h][1] in range(xw[w][0],xw[w][1]+1):
#             chat += (xh[h][1] - xh[h][0])
#             h += 1
#         else:
#             chat += (xw[w][1] - xh[h][0])
#             w += 1
#     elif xh[h][1] in range(xw[w][0],xw[w][1]+1):
#         chat += (xh[h][1] - xw[w][0])
#         h += 1
#     elif xw[w][0] in range(xh[h][0],xh[h][1]+1) and xw[w][1] in range(xh[h][0],xh[h][1]+1):
#         chat += (xw[w][1] - xw[w][0])
#         w += 1
#     else:
#         w += 1
# print(chat)
'''
4
1 3
5 6
9 13
14 15
2 3
5 6
10 11
13 14

4
1 3
5 6
9 13
14 15
2 4
5 7
10 11
13 14
'''