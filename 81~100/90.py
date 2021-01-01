a, r, n = map(int, input().split())
count = 0

while True:
    count += 1
    if count == n:
        print(a)
        break
    a *= r

# 등비수열의 합 공식을 이용한 풀이
a, r, n = map(int, input().split())
print(a * (r ** (n - 1)))