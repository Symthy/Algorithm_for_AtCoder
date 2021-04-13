"""
https://atcoder.jp/contests/abc077/tasks/arc084_a
"""

from bisect import bisect_left, bisect_right

n = int(input())
top_list = sorted(list(map(int, input().split())))
middle_list = sorted(list(map(int, input().split())))
under_list = sorted(list(map(int, input().split())))
result = [bisect_left(top_list, m) * (n - bisect_right(under_list, m)) for m in middle_list]
print(result)
print(sum(result))
