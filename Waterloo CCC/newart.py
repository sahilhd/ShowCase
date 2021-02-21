import sys
sys.setrecursionlimit(2000)


m = int(input())
n = int(input())
k = int(input())
Counter = 0

canvas = [[False for i in range(int(n))] for r in range(int(m))]

for i in range(k):
    C = input()
    C = C.split(' ')

    if (C[0] == 'C'):
        for x in range(m):
                canvas[x][int(C[1]) - 1] = not canvas[x][int(C[1]) - 1]

    else:
        for x in range(n):
            canvas[int(C[1]) - 1][x] = not canvas[int(C[1]) - 1][x]

for i in range(m):
    for r in range(n):
        if (canvas[i][r] == True):
            Counter += 1



print(Counter)