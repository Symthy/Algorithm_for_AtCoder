"""
ビット全探索
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
"""


def bit_search(i, m, n, A):
    if m == 0:
        return True
    if i >= n:
        return False
    result = bit_search(i + 1, m, n, A) or bit_search(i + 1, m - A[i], n, A)
    return result


def main():
    n = int(input())
    A = list(map(int, input().split()))
    m_num = int(input())
    m_array = list(map(int, input().split()))

    for m in m_array:
        if bit_search(0, m, n, A):
            print("yes")
        else:
            print("no")


main()
