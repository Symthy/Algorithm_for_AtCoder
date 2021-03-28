
n = int(input())
array = list(map(int, input().split()))

alice_num = 0
bob_num = 0
loop_count = 0

for i in range(n):
    max_val = max(array)
    if i % 2 == 0:
        alice_num += max_val
    else:
        bob_num += max_val
    array.remove(max_val)
    loop_count += 1


print(alice_num - bob_num)
