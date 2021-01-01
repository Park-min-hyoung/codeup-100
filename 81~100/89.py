a, d, n = map(int, input().split())
count = 0

while True:
    count += 1
    if count == n:
        print(a)
        break
    a += d

# 등차 수열 합공식을 이용한 풀이
a, d, n = map(int, input().split())
print(a + d * (n - 1))
