n, k = map(int, input().split())
a = list(map(int, input().split()))

avg = k // n
sur = k % n
people = {a[i]: avg for i in range(n)}

sorted_a = sorted(a)
for i in range(sur):
    people[sorted_a[i]] += 1

for i in range(n):
    print(people[a[i]])
