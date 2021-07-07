"""
https://atcoder.jp/contests/abc128/tasks/abc128_c
"""
import copy


# light_on_count_list: 電球毎のスイッチONの数（サイズ：電球の数）
def switch_bit_search(switch_index, is_on, light_on_count_list, N_switch_num, M_light_num, ks, p):
    for m in range(M_light_num):
        if not is_on:
            break
        switch_nums = ks[m][1:]
        for num in switch_nums:
            if switch_index == num:
                light_on_count_list[m] += 1

    if switch_index == N_switch_num:
        for i in range(M_light_num):
            switch_on_count = light_on_count_list[i]
            if switch_on_count % 2 != p[i]:
                return 0
        return 1

    light_on_count_list1 = copy.deepcopy(light_on_count_list)
    light_on_count_list2 = copy.deepcopy(light_on_count_list)
    result = switch_bit_search(switch_index + 1, True, light_on_count_list1, N_switch_num, M_light_num, ks,
                               p) + switch_bit_search(switch_index + 1, False, light_on_count_list2, N_switch_num, M_light_num, ks, p)
    return result


def main():
    N_switch_num, M_light_num = map(int, input().split())
    ks = []
    for _ in range(M_light_num):
        ks.append(list(map(int, input().split())))
    p = list(map(int, input().split()))

    total = switch_bit_search(1, True, [0] * M_light_num, N_switch_num, M_light_num, ks,
                              p) + switch_bit_search(1, False, [0] * M_light_num, N_switch_num, M_light_num, ks, p)

    print(total)


main()
