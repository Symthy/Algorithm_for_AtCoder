
N = int(input())

result = False
for i in range(1, 10, 1):
    if N % i == 0 and N // i <= 9:
        result = True
        break

print('Yes' if result else 'No')
