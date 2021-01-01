n = int(input())
plate = [[0] * 19 for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    plate[x - 1][y - 1] = 1

for i in range(19):
    for j in range(19):
        print(plate[i][j], end = ' ')
    print()