"""
https://atcoder.jp/contests/agc020/tasks/agc020_a
Aliceが先手である以上、ぶつかった時に逆方向にしか進めない方が負け
"""

N, A, B = map(int, input().split())

if abs(A - B) % 2 == 1:
    print('Borys')
else:
    print('Alice')
