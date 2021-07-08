"""
順列全探索
https://atcoder.jp/contests/abc145/tasks/abc145_c
"""

import itertools
import math

N = int(input())
coordinate_list = []
for _ in range(N):
    coordinate_list.append(list(map(int, input().split())))

permutations_list = itertools.permutations([i for i in range(N)])  # 全順列生成


total_distance = 0
for one_case in permutations_list:
    distance = 0
    for i in range(N):
        if i >= N - 1:
            break
        x1 = coordinate_list[one_case[i]][0]
        y1 = coordinate_list[one_case[i]][1]
        x2 = coordinate_list[one_case[i+1]][0]
        y2 = coordinate_list[one_case[i+1]][1]
        distance += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    total_distance += distance

print(total_distance/math.factorial(N))  # math.factorial：階乗
