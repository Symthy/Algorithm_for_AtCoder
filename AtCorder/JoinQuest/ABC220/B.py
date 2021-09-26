def convert_n_to_10(X, n):
    ans = 0
    num_str = str(X)
    for i in range(len(num_str), 0, -1):
        ans += int(num_str[i-1]) * (n ** (len(num_str) - i))
    return ans


def main():
    K = int(input())
    A, B = map(int, input().split())

    a_base_ten = convert_n_to_10(A, K)
    b_base_ten = convert_n_to_10(B, K)

    print(a_base_ten * b_base_ten)


main()
