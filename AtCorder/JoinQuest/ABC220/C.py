def main():
    N = int(input())
    A_list: List[int] = list(map(int, input().split()))
    X = int(input())

    a_sum = 0
    for i in range(N):
        a_sum += A_list[i]

    ans = (X // a_sum) * N
    a_sum = a_sum * (X // a_sum)

    for a in A_list:
        a_sum += a
        ans += 1
        if X < a_sum:
            break

    print(ans)


main()
