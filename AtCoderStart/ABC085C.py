
n = int(input())
y = int(input())

is_exist = False

for i in range(n+1):
    for j in range(n - i):
        k = 9 - i - j
        if 10000 * i + 5000 * j + 1000 * k == y:
            is_exist = True
            print(str(i) + ' ' + str(j) + ' ' + str(k))
    if is_exist == True:
        break

if is_exist == False:
    print('-1 -1 -1')
