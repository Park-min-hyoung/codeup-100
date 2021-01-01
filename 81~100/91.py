a, m, d, n = map(int, input().split())
data = a

for i in range(n - 1):
    data = (data * m) + d
print(data)