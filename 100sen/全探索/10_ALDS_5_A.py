"""
ビット全探索
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
"""


def solve(i, m, n, A):
    if m == 0:
        return True
    if i >= n:
        return False
    res = solve(i + 1, m, n, A) or solve(i + 1, m - A[i], n, A)
    return res


def main():
    n = int(input())
    A = list(map(int, input().split()))
    m_num = int(input())
    m_array = list(map(int, input().split()))

    for m in m_array:
        if solve(0, m, n, A):
            print("yes")
        else:
            print("no")


main()
