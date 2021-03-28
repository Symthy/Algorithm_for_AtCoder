
n = int(input())
a = int(input())
b = int(input())

result = 0

for i in range(n):
    value = i + 1
    sum = int(value / 10) + value % 10
    if sum >= a and sum <= b:
        result += value

print(result)
