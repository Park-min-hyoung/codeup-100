data = [int(x) for x in input().split()]

print(data[0] + data[1], data[0] - data[1], data[0] * data[1], data[0] // data[1], data[0] % data[1], sep='\n')
print('%.2f' %(data[0] / data[1]))