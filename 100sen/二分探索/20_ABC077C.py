"""
https://atcoder.jp/contests/abc077/tasks/arc084_a
"""

n = int(input())
top_list = list(map(int, input().split()))
#middle_list = list(map(int, input().split()))
#under_list = list(map(int, input().split()))

top_list.sort()
# middle_list.sort()
# under_list.sort()

# if middle > top
# if under > middle


def get_comb_all(array, n, sum=0):
    comb_list = []
    print(array, n, sum)
    for i in range(n):
        comb_list.append(sum + array[i])
        if i + 1 == n:
            break
        comb_list = comb_list + \
            get_comb_all(array[i + 1:], n - i - 1, sum + array[i])
    return comb_list


print(get_comb_all(top_list, n))
