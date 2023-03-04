# ref: https://note.com/syamashi/n/na912caf78950
#
# Q.2
# atcoder
# ?????
#
# S'を書き出す
# i=0:   coder
# i=1: a  oder
# i=2: at  der
# i=3: atc  er
# i=4: atco  r
# i=5: atcod
#
# index[i]の一文字だけ状態変化している。
# i=0のときだけ、T文字との誤りをカウントして、
# iの変化時に、変化箇所だけ判定しなおしばよさそう。

# ref: https://atcoder.jp/contests/abc287/submissions/38439317
S = ['_'] + list(input())
T = ['_'] + list(input())
N = len(S) - 1  # 1-index
M = len(T) - 1  # 1-index
 
# SとTの先頭何文字まで一致しているか予め計算しておく（Q2のi=5）
top = [False] * (M+1)
top[0] = True
for x in range(1, M+1):
    if top[x-1] and (S[x] == T[x] or S[x] == '?' or T[x] == '?'):
        top[x] = True
    else:
        break
 
# SとTの末尾何文字まで一致しているか予め計算しておく（Q2のi=0）
bottom = [False] * (M+1)
bottom[0] = True
for x in range(1, M+1):
    if bottom[x-1] and (S[N-x+1] == T[M-x+1] or S[N-x+1] == '?' or T[M-x+1] == '?'):
        bottom[x] = True
    else:
        break

# Q2の i=0 と i=5 の状態から２つ同時に変化する部分を見ていっている
for i in range(M+1):
    if top[i] and bottom[M-i]:
        print("Yes")
    else:
        print("No")