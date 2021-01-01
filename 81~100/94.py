n = int(input())
num = [int(x) for x in input().split()]
num.reverse()

for i in num:
    print(i, end = ' ')