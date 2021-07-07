"""
ビット探索（元：10_ALDS_5_A.py）
i：Aの何番目見てるか、m：判定対象の数値、n：入力値の数、A：素材の数値一覧
"""


def bit_search(i, m, n, A):
    if m == 0:
        return True
    if i >= n:
        return False
    result = bit_search(i + 1, m, n, A) or bit_search(i + 1, m - A[i], n, A)
    return result
