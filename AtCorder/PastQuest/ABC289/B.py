M, N = map(int, input().split())
a_arr = list(map(int, input().split()))

g = []
edge = set()
before = 0
for i in range(N):
    node = a_arr[i]
    if i == 0:
        edge.add(node)
        edge.add(node + 1)
    if node == before + 1:
        edge.add(node)
        edge.add(node + 1)
    else:
        g.append(edge)
        edge = set()
        edge.add(node)
        edge.add(node + 1)
    if i == N - 1:
        g.append(edge)
        break
    before = node

ans = []
for gi in g:
    li = list(gi)
    for i in range(len(li) - 1, -1, -1):
        ans.append(str(li[i]))

print(" ".join(ans))
