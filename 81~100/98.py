a, b = map(int, input().split())
plate = [[0] * b for _ in range(a)]
n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0: plate[x - 1][y - 1 + j] = 1
        else: plate[x - 1 + j][y - 1] = 1

for i in range(a):
    for j in range(b):
        print(plate[i][j], end = ' ')
    print()