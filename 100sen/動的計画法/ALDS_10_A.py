"""
フィボナッチ数列
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja
"""

result_list = [-1] * 44
result_list[0] = 1
result_list[1] = 1


def fibonacci(n: int):
    if n == 0 or n == 1:
        return 1

    r1 = result_list[n-1] if result_list[n-1] != -1 else fibonacci(n-1)
    r2 = result_list[n-2] if result_list[n-2] != -1 else fibonacci(n-2)
    result = r1 + r2
    result_list[n] = result
    return result


def main():
    n = int(input())
    print(fibonacci(n))


main()
