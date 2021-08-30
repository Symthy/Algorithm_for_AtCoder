
a, b, k = map(int, input().split())

cf = []
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        cf.append(i)

print(cf[len(cf) - k])
