"""
https://atcoder.jp/contests/abc077/tasks/arc084_a
3段の祭壇（中断は上段より大きく、下段は中断より大きくなければならない）

bisect：https://at274.hatenablog.com/entry/2018/01/12/090000
"""

from bisect import bisect_left, bisect_right

n = int(input())
top_list = sorted(list(map(int, input().split())))
middle_list = sorted(list(map(int, input().split())))
under_list = sorted(list(map(int, input().split())))
result = [bisect_left(top_list, m) * (n - bisect_right(under_list, m)) for m in middle_list]
print(result)
print(sum(result))
