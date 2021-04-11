"""
https://atcoder.jp/contests/abc106/tasks/abc106_b
"""

n = int(input())

max = int(n / 2)
#results = []
count = 0

for odd in range(1, n+1, 2):
    i = 1
    for num in range(1, max + 1):
        if odd % num == 0:
            i += 1
    # if i == 8:
    #    results.append(odd)
    count += 1 if count == 8 else 0

# print(len(results))
print(count)
