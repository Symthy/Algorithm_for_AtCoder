
N = int(input())
dictionary = {}
for _ in range(N):
    s = input()
    if not s in dictionary:
        dictionary[s] = ''
    else:
        dictionary.pop(s)

print(len(dictionary))
