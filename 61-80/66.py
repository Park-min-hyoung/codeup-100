data = [int(x) for x in input().split()]

for i in range(len(data)):
    print('odd') if data[i] % 2 == 1 else print('even')