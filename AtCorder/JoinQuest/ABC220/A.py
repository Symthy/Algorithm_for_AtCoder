def main():
    A, B, C = map(int, input().split())

    i = 1
    is_out = False
    while True:
        ans = C * i
        if ans >= A and ans <= B:
            print(ans)
            is_out = True
            break
        if ans > B:
            break
        i += 1

    if is_out == False:
        print('-1')


main()
