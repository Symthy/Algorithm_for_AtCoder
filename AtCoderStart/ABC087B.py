a = int(input())  # 500
b = int(input())  # 100
c = int(input())  # 50
x = int(input())

if a * 500 + b * 100 + c * 50 < x:
    print(0)

count = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500 * i + 100 * j + 50 * k == x:
                count += 1

print(count)
