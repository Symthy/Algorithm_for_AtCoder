
n = int(input())
c = list(map(int, input().split()))
sorted_c = sorted(c)

result = 1
for i in range(n):
    result *= sorted_c[i] - i

print(result % (10**9+7))
