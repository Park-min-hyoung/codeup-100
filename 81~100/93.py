n = int(input())
call_number = [int(x) for x in input().split()]
student_number = [0] * 23

for i in range(len(call_number)): student_number[i] = call_number.count(i + 1)

for i in student_number: print(i, end = ' ')