n = int(input())
array = list(map(int, input().split()))

value_dict = {}

for i in range(n):
    value_dict[array[i]] = 1

print(len(value_dict))
