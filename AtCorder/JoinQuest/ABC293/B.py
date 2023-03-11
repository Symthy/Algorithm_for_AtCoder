N = int(input())

arr_a = list(map(int, input().split()))

called = [0] * N

for i in range(N):
    if called[i] == 1:
        continue
    called[arr_a[i] - 1] = 1

ans = []
for i in range(N):
    if called[i] == 0:
        ans.append(str(i + 1))

print(len(ans))
print(" ".join(ans))
