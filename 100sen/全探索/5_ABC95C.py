"""
https://atcoder.jp/contests/abc095/tasks/arc096_a
"""


def main():
    a, b, c, x, y = map(int, input().split())
    ab = c * 2

    result1 = a * x + b * y
    result2 = ab * (x if x > y else y)
    result3 = ab * (x if x < y else y) + (a * (x-y) if x > y else b * (y-x))

    print(min(result1, result2, result3))


main()

# 以下３パターンしかない
# A * X + B * Y
# AB * 2 * max(X,Y)
# AB * 2 * min(X,Y) + (A * X or B * Y)
