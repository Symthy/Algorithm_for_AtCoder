
n = int(input())
li = list(map(int, input().split()))
count = 0

while True:
    li_convert = []
    is_continue = True
    for i in range(n):
        if li[i] % 2 != 0:
            is_continue = False
            break
        else:
            li_convert.append(li[i]/2)

    if is_continue == False:
        break

    count += 1
    li = li_convert

print(count)
