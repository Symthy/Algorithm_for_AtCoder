
a, b, c = map(int, input().split())

max_val = max([a, b, c])
dist = abs(max_val - a) + abs(max_val - b) + abs(max_val - c)
result = dist // 2
if dist % 2 == 1:
    result += 2

print(result)
