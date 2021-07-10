

def main():
    N = int(input())
    t = [0]
    x = [0]
    y = [0]
    for _ in range(N):
        ti, xi, yi = map(int, input().split())
        t.append(ti)
        x.append(xi)
        y.append(yi)

    result = True
    for i in range(N):
        dt = t[i + 1] - t[i]
        dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
        if (dist > dt or (dist % 2 != dt % 2)):
            result = False
            break

    print('Yes' if result else 'No')


main()
