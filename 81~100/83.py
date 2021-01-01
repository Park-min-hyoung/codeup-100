n = int(input())

for i in range(1, n + 1):
    print(i, end = ' ') if i % 3 != 0 else print('X', end = ' ')