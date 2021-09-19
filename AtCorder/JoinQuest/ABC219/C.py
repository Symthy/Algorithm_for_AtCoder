import heapq


def botu():
    X = input().lower()
    N = int(input())

    sort_dict = {}
    for i in range(len(X)):
        sort_dict[X[i]] = str(i+1)

    order_to_input_dict = {}
    order_weight_key_list = []
    heapq.heapify(order_weight_key_list)
    for _ in range(N):
        Si = input()
        order_weight_key_str = ''
        for j in range(len(Si)):
            order_weight_key_str += sort_dict[Si[j]].zfill(2)
        order_weight_key = int(order_weight_key_str)
        order_to_input_dict[order_weight_key] = Si
        heapq.heappush(order_weight_key_list, order_weight_key)

    for _ in range(len(order_weight_key_list)):
        order_weight_key = heapq.heappop(order_weight_key_list)
        print(order_to_input_dict[order_weight_key])


def main():
    X = input()
    N = int(input())
    sort_dict = {}
    recovert_dict = {}
    for i in range(len(X)):
        sort_dict[X[i]] = i + 1
        recovert_dict[i+1] = X[i]
    l_2d = []
    for _ in range(N):
        Si = input()
        converted_num = []
        for j in range(len(Si)):
            converted_num.append(sort_dict[Si[j]])
        l_2d.append(converted_num)

    l_2d.sort()
    for i in range(len(l_2d)):
        line = ''
        converted_num = l_2d[i]
        for j in range(len(converted_num)):
            line += recovert_dict[converted_num[j]]
        print(line)


main()
