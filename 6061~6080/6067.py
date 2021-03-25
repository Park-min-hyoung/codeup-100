num = int(input())

if num < 0:
    print("A") if num % 2 == 0 else print("B")
else:
    print("C") if num % 2 == 0 else print("D")