from collections import deque


# N: ボールの種類
# M: 筒(tube)の数
# k: 筒の中のボールの数
# a_list: 筒の中の各ボールの色
def main():
    tubes = {}  # key: M(筒)のインデックス、val：筒(deque)
    tube_top_ball_map = {}  # key:int（ボールの色番号）, val:array[int]（筒のindex）
    top_same_ball_comb_tube = deque([])

    N, M = map(int, input().split())
    for i in range(M):
        k = int(input())
        a_list = list(map(int, input().split()))
        que = deque(a_list, k)
        if not a_list[0] in tube_top_ball_map:
            tube_top_ball_map[a_list[0]] = [i]
        else:
            tube_top_ball_map[a_list[0]].append(i)
        tubes[i] = que

    tube_top_same_ball_num_que = deque()
    for ball_num, tube_indexes in tube_top_ball_map.items():
        if len(tube_indexes) == 2:
            tube_top_same_ball_num_que.append(ball_num)

    while len(tube_top_same_ball_num_que) != 0:
        ball_num = tube_top_same_ball_num_que.popleft()
        M_indexes = tube_top_ball_map[ball_num]

        tube1_index = M_indexes[0]
        tubes[tube1_index].popleft()
        if len(tubes[tube1_index]) == 0:
            tubes.pop(tube1_index)
        else:
            tube1_top_ball_num = tubes[tube1_index][0]
            if not tube1_top_ball_num in tube_top_ball_map:
                tube_top_ball_map[tube1_top_ball_num] = [tube1_index]
            else:
                tube_top_ball_map[tube1_top_ball_num].append(tube1_index)
            if len(tube_top_ball_map[tube1_top_ball_num]) == 2:
                tube_top_same_ball_num_que.append(tube1_top_ball_num)

        tube2_index = M_indexes[1]
        tubes[tube2_index].popleft()
        if len(tubes[tube2_index]) == 0:
            tubes.pop(tube2_index)
        else:
            tube2_top_ball_num = tubes[tube2_index][0]
            if not tube2_top_ball_num in tube_top_ball_map:
                tube_top_ball_map[tube2_top_ball_num] = [tube2_index]
            else:
                tube_top_ball_map[tube2_top_ball_num].append(tube2_index)
            if len(tube_top_ball_map[tube2_top_ball_num]) == 2:
                tube_top_same_ball_num_que.append(tube2_top_ball_num)

        tube_top_ball_map.pop(ball_num)

    if len(tubes) == 0:
        print('Yes')
    else:
        print('No')


main()
