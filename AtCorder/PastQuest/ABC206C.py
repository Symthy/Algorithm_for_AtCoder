n = int(input())
a_list = sorted(list(map(int, input().split())))

all_num = n * (n - 1) / 2

a_list.append(-1)
cnt = 1
for i in range(n):
    if a_list[i] == a_list[i + 1]:
        cnt += 1
    else:
        all_num -= (cnt * (cnt - 1) / 2)
        cnt = 1

print(int(all_num))
