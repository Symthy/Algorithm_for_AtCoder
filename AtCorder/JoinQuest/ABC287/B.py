def main():
    N, M = map(int, input().split())
    arr_S = []
    arr_T = []
    for i in range(N):
        arr_S.append(input())
    for i in range(M):
        arr_T.append(input())

    sum = 0
    for s in arr_S:
        if s[3:] in arr_T:
            sum += 1
    print(sum)

main()