def main():
    alpha_list = 'abcdefghijklmnopqrstuvwxyz'
    p_list = list(map(int, input().split()))

    ans = ''
    for p in p_list:
        ans += alpha_list[p - 1]
    print(ans)


main()
