"""
1～Nの長さの配列から、1個～N個の要素を組み合わせた合計値の一覧を返す
"""


def get_comb_all(array, n, sum=0):
    comb_list = []
    for i in range(n):
        comb_list.append(sum + array[i])
        if i + 1 == n:
            break
        comb_list = comb_list + get_comb_all(array[i + 1:], n - i - 1, sum + array[i])
    return comb_list
