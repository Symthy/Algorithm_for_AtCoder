N = int(input())

result = 0
for i in range(1, N + 1, 2):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt % 8 == 0:
        result += 1

print(result)
