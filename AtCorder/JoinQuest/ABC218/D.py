# 長さが一致する２つの組みを見つければいい
# diff を管理すればいいはず？

def main():
    N = int(input())

    x_map = {}
    x_to_yend_diff_map = {}
    for i in range(N):
        x, y = map(int, input().split())

        if not x in x_map:
            x_map[x] = [y]
            x_to_yend_diff_map[x] = {}
        else:
            for y_i in x_map[x]:
                y_end = y_i if y_i > y else y
                y_end_diff_key = str(y_end) + ':' + str(abs(y_i - y))
                x_to_yend_diff_map[x][y_end_diff_key] = abs(y_i - y)
            x_map[x].append(y)

    comb_set = set()
    for x, yend_diff_map in x_to_yend_diff_map.items():
        for x2, yend_diff_map2 in x_to_yend_diff_map.items():
            if x >= x2:
                continue
            for key, diff in yend_diff_map.items():
                if key in yend_diff_map2 and yend_diff_map2[key] == diff:
                    comb_set.add(str(x) + ':' + str(x2))

    print(len(comb_set))


main()
