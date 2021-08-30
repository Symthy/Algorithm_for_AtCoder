"""
https://atcoder.jp/contests/agc010/tasks/agc010_a
奇数２つを足せば偶数になる
偶数は何個あっても２つ足し合わせていけば最後は１つになるので、
奇数の数だけを見ればいい
NOになるケースは奇数１つ、偶数１つが残る時
"""


N = int(input())
li = list(map(int, input().split()))

odd_count = 0
for i in range(N):
    if li[i] % 2 == 1:
        odd_count += 1

odd_count = odd_count % 2

result = True
if odd_count == 1:
    result = False

print('YES' if result else 'NO')
