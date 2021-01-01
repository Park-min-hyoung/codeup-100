n = int(input(), 16)

for x in range(1, 16):
    print('%X*%X=%X' %(n, x, (n * x)))