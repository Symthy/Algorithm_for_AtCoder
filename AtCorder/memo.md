# Python Tips

二分探索は bisect

# Memo

## ABC 206 C

A = (A1, A2, A3, ..., An)
1 <= i <= j <= N

i より後ろにある数の合計だから

N = 10 の時
組合数は 10 + 9 + 8 + 7 + … = n*(n-1)/2

重複除去は、set に格納だと TLE起す
重複を意識する場合は、ソートしてから捌けばいける

## ABC 207 C

# 問題分類

## DP

### 配るDP
- ABC220 D

## 再起
デフォルト上限1000だから増やさないと失敗する

```
import sys
sys.setrecursionlimit(300000)
```
