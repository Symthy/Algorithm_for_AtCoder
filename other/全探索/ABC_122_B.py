
s_list = list(input())

count = 0
result = 0
for s in s_list:
    if s in 'ACGT':
        count += 1
        result = max(result, count)
    else:
        count = 0

print(result)
