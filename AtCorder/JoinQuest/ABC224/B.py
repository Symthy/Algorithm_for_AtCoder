def main():
    H, W = map(int, input().split())

    a_list = []
    for i in range(H):
        row_list = list(map(int, input().split()))
        a_list.append(row_list)

    is_ok = True
    for i1 in range(0, H - 1):
        for i2 in range(1, H):
            if i1 >= i2:
                continue
            for j1 in range(0, W - 1):
                for j2 in range(1, W):
                    if j1 >= j2:
                        continue
                    if not a_list[i1][j1] + a_list[i2][j2] <= a_list[i2][j1] + a_list[i1][j2]:
                        is_ok = False
                        break
                if is_ok == False:
                    break
            if is_ok == False:
                break
        if is_ok == False:
            break

    print('Yes' if is_ok else 'No')


main()
